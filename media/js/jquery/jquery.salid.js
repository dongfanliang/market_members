/**
 * jQuery Salid (Simple Validation) Plugin 1.0.0
 *
 * http://www.jqueryin.com/projects/salid-the-simple-jquery-form-validator/
 * http://plugins.jquery.com/project/Salid
 *
 * Copyright (c) 2009 Corey Ballou
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
(function($) {
	var hasErrors = false;
	var errors = [];
	
	/* validate entire form */
	$.fn.salidate = function(elemsToValidate, errorCallback) {
		var $form = $(this);
		if (!$form.is('form')) {
			console.log('The salidate function only works with forms.');
			return false;
		}
		if (typeof errorCallback != 'function') errorCallback = salid_errorHandler;
		$form.submit(function() {
			$.each(elemsToValidate, function(field, params) {
				validate(field, params, $form);
			});
			return (hasErrors) ? handleErrors(errorCallback, $form) : true;
		});
	}

	/* validate individual elements */
	$.fn.salid = function(event, params, errorCallback) {
		var tagname = this.get(0).tagName.toLowerCase();
		var validElems = {
			input: ['blur','keydown','keyup'],
			select: ['change','blur'],
			textarea: ['blur','focus','keydown','keyup']
		};
		if (typeof validElems[tagname] == 'undefined') {
			console.log(escape(tagname) + ' cannot be used to for singular validation.');
			return false;
		}
		event = event || 'blur';
		if (!$.inArray(validElems[tagname], event)) {
			console.log('You cannot bind the event ' + escape(event) + ' to the tag ' + escape(tagname));
			return false;
		}
		if (typeof errorCallback != 'function') errorCallback = salid_errorHandler;
		if (typeof params == 'String' && params == 'unbind') {
			this.each(function() { $(this).unbind(event); });
			return false;
		}
		if (typeof params == 'undefined') params = {};
		this.each(function() {
			var $this = $(this);
			$this.bind(event, function() {
				if (!validate($this, params)) {
					handleErrors(errorCallback, $this);
				}
			});
		});
	}
	
	/* handle validation type */
	function validate(field, params, $form) {
		var valid = true;
		if (typeof params.callbacks != 'undefined' && params.callbacks.constructor == Array) {
			$.each(params.callbacks, function(idx, rule) {
				if (!_validate(field, rule, $form)) valid = false;
			});
			return valid;
		} else return _validate(field, params, $form);
	}
	
	/* run a validation function */
	function _validate(field, params, $form) {
		var fcn, $field, rules, singlerule = false;
		var obj = (function() { return this; })();
		var defaults = { callback : 'required', callbackParams : null, msg : 'This field is required' };
		if (field instanceof jQuery) {
			singlerule = true;
			$field = field;
			field = field.attr('id') || field.attr('name');
		} else $field = getElem($form, field);
		// pass over disabled fields
		if ($field.attr('disabled') == false) {
			// remove any old preexisting errors
			if ($field.is(':radio') || $field.is(':checkbox')) {
				$field.parent('label').removeClass('error').next('span.error').remove();
			} else {
				$field.removeClass('error').parent().find('span.error').remove();
			}
			rules = $.extend({}, defaults, params);
			rules = $.metadata ? $.extend({}, rules, $field.metadata()) : rules;
			fcn = 'salid_' + rules.callback;
			if (typeof obj[fcn] != 'function') {
				console.log('It does not appear as though the validation function ' + fcn + ' exists.');
				return false;
			}
			if (!obj[fcn]($field, rules.callbackParams)) {
				addError(field, $field, rules.msg);
				hasErrors = true;
				return false;
			}
		}
		return true;
	}

	/* add an error */
	function addError(field, $field, msg) {
		var fixed = field.replace(/\[/i, 'OB');
		fixed = fixed.replace(/\]/i, 'CB');
		errors[ errors.length ] = { elem: $field, field: field, msg: msg };
	}

	/* handle errors by calling a callback function */
	function handleErrors(errorCallback, $elem) {
		var e, i = errors.length;
		while(i--) { e = errors[i]; $(e.elem).addClass('error'); }
		errorCallback($elem, errors);
		hasErrors = false;
		errors = [];
		return false;
	}

	/* Attempt to find the form element by id with fallback on name. */
	function getElem($elem, field) {
		if ($elem.get(0).tagName.toLowerCase() != 'form') return $elem;
		if (field instanceof jQuery) return field;
		field = field.replace(/(\[(.*)?\])/, '');
		var $found = $elem.find("#"+field);
		if ($found.length == 0) $found = $elem.find("*[name^='"+field+"']");
		return $found;
	}
	
})(jQuery);

/* default error handler popup */
function salid_errorHandler($elem, errors) {
	var isformelem, $e, e, i = errors.length;
	isformelem = $elem.get(0).tagName.toLowerCase() != 'form';
	while(i--) {
		e = errors[i];
		$e = $(e.elem);
		if ($e.is(':radio') || $(e).is(':checkbox')) {
			$e.parent('label').addClass('error').after('<span class="error"><span>' + e.msg + '</span></span>');
		} else {
			$e.addClass('error').parent().append('<span class="error"><span>' + e.msg + '</span></span>');
		}
	}
	return false;
}

/* required */
function salid_required(field, params) {
	if (field.length == 0 || typeof field == 'undefined') return false;
	if (/radio|checkbox/i.test(field[0].type)) return (field.filter(':checked').length > 0);
	return (field.length > 0 && field.val() != '');
}
/* minlength */
function salid_minlength(field, params) {
	return (!salid_required(field, params) || field.val().length >= params);
}
/* maxlength */
function salid_maxlength(field, params) {
	return (!salid_required(field, params) || field.val().length <= params);
}
/* email */
function salid_email(field, params) {
	return (!salid_required(field, params) || /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i.test(field.val()));
}
/* phone */
function salid_phone(field, params) {
	var filter = /(\+\d)*\s*(\(\d{3}\)\s*)*\d{3}(-{0,1}|\s{0,1})\d{2}(-{0,1}|\s{0,1})\d{2}/;
	return (!salid_required(field, params) || filter.test(field.val()));
}
/* url */
function salid_url(field, params) {
	return (!salid_required(field, params) || /(https?|s?ftp):\/\//i.test(field.val()));
}
/* zipcode */
function salid_zipcode(field, params) {
	return (!salid_required(field, params) || /(^\d{5}(-\d{4})?)$/.test(field.val()));
}
/* alpha */
function salid_alpha(field, params) {
	return (!salid_required(field, params) || /^[A-Za-z]+$/.test(field.val()));
}
/* numeric */
function salid_numeric(field, params) {
	return (!salid_required(field, params) || /^[\d]+$/.test(field.val()));
}
/* alpha-numeric */
function salid_alphanumeric(field, params) {
	return (!salid_required(field, params) || /^[A-Za-z0-9]+$/i.test(field.val()));
}
/* alpha-dash (alpha-numeric with dashes and underscores allowed). */
function salid_alphadash(field, params) {
	return (!salid_required(field, params) || /^[A-Za-z0-9-_]+$/i.test(field.val()));
}
/* matching values */
function salid_match(field, params) {
	if (typeof field == 'undefined') return false;
	var field2 = field.siblings('#' + params);
	if (field2.length == 0) field2 = field.siblings("*[name^='"+params+"']");
	if (field2.length == 0) return false;
	return (field.val() == field2.val());
}
