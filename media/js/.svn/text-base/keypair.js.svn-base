function CheckTitle(myCheck, checkId)
{
	var checkAll = document.getElementsByName(myCheck);
	var checkTitle = document.getElementById(checkId);
	for (var i = 0; i < checkAll.length; i++)
        checkAll[i].checked = checkTitle.checked;
}

function deletekeypair(id, formId, url)
{
	var keypair = document.getElementsByName(id);
	for (var i = 0; i < keypair.length; i++)
	{
		if (keypair[i].checked)
		{
			if(confirm("确定要删除吗？"))
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
