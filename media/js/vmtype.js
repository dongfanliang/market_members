function vmtype_edit(cbname, formId, url)
{
	var vmType = document.getElementsByName(cbname);
	for (var i = 0; i < vmType.length; i++)
	{
		if (vmType[i].checked)
		{
			var myForm = document.getElementById(formId);
			myForm.action = url;
			myForm.submit();

			return;
		}
	}
	alert("请选择需要编辑的资源类型！");
}

function vmtype_delete(cbname,formId,url)
{
	var vmType = document.getElementsByName(cbname);
	for (var i = 0; i < vmType.length; i++)
	{
		if (vmType[i].checked)
		{
			if (confirm("确定要删除吗？"))
			{
				var myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			return;
		}
	}
	alert("请选择需要删除的资源类型！");
}
