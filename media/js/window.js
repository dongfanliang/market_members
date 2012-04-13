$(function(){
   	  function winResizeHandler() {
		  $(".sidebar").height($(window).height() - $(".footer").height() - $(".header").height() -2) ;
		  $(".sidebar-div").height($(window).height() - $(".footer").height() - $(".header").height() - $(".sidebar-title").height() -4) ;
		  $(".ico-img").height($(window).height() - $(".footer").height() - $(".header").height() -2) ;
		  $(".conment-div").height($(window).height() - $(".footer").height() - $(".header").height() - $(".conment-title").height() -4) ;
		  
		  $(".conment").width($(window).width() - $(".sidebar").width() - $(".ico-img").width()) ;
		  $(".conment-div").width($(window).width() - $(".sidebar").width() - $(".ico-img").width() -1) ;
		  $(".conment-title").width($(window).width() - $(".sidebar").width() - $(".ico-img").width()) ;
	  }
	  winResizeHandler();
	  $(window).resize(winResizeHandler) ;  	 
   });

function selectOne(obj)
{
	var objCheckBox = document.getElementsByName("cb"); 
	for(var i=0;i<objCheckBox.length;i++){ 
	   //判断复选框集合中的i元素是否为obj，若为否则便是未被选中 
		if (objCheckBox[i]!=obj) { 
			objCheckBox[i].checked = false; 
		} else{ 
		//若是，原先为被勾选的变成勾选，反之则变成未勾选 
		 objCheckBox[i].checked = obj.checked; 
	   } 
	} 
} 
