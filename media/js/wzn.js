function stopInstance(instanceID, formInstance, url)
{
	var count = 0;
	var namebox = document.getElementsByName(instanceID);
	for (var i = 0; i < namebox.length; i++)
	{
		if (namebox[i].checked)
		{
			count++;
		}
	}
	if (count == 0) 
	{
		alert("请选择要停止的实例！");
	}
	else
	{
		if(confirm("确定要停止吗？"))
		{
			var myform = document.getElementById(formInstance);
			myform.action = url;
			myform.submit();
		}
		else
		{
			return;
		}
	}
}

