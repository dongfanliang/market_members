function CheckTitle(myCheck, checkId)
{
    var checkAll = document.getElementsByName(myCheck);
    var checkTitle = document.getElementById(checkId);
    for (var i = 0; i < checkAll.length; i++)
		checkAll[i].checked = checkTitle.checked;
}

function revokerule(id, formId, url)
{
	var rule = document.getElementsByName(id);
	for (var i = 0; i < rule.length; i++)
	{
		if (rule[i].checked)
		{
			if (confirm("确定要删除吗？"));
			{
				var myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			return;
		}
	}
	alert("请选择要删除的内容！");
}
