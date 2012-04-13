function show_release(cbname,formId,url)
{
	var ippool = document.getElementsByName(cbname);
	for (var i = 0; i < ippool.length; i++)
	{
		if (ippool[i].checked)
		{
			var ippoolFields = ippool[i].value.split(' ');
			if (ippoolFields[1] == "available")
			{
				if (confirm("确定要释放"+ippool[i].value+"吗？"))
				{
					var myForm = document.getElementById(formId);
					myForm.action = url;
					myForm.submit();
				}
			}
			else if (ippoolFields[1] == "nobody")
				alert("该IP未被分配，不需要释放！");
			else
				alert("请先取消关联再释放ip！");
			return;
		}
	}
	alert("请选择需要关联的IP地址！");
}

function show_associate(cbname, formId, url)
{
	var ippool = document.getElementsByName(cbname);
	for (var i = 0; i < ippool.length; i++)
	{
		if (ippool[i].checked)
		{
			var ippoolFields = ippool[i].value.split(' ');
			if (ippoolFields[1] == "available")
			{
				myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			else if (ippoolFields[1] == "nobody")
				alert("未分配IP，请您分配后再关联！");
			else
				alert("已经关联，请重新操作为！");
			return;
		}
	}
	alert("请选择需要关联的IP地址！")
}

function show_disassociate(cbname, formId, url)
{
	var ippool = document.getElementsByName(cbname);
	for (var i = 0; i < ippool.length; i++)
	{
		if (ippool[i].checked)
		{
			var ippoolFields = ippool[i].value.split(' ');
			if (ippoolFields[1] != "nobody")
			{
				if (confirm("确定要取消" + ippool[i].value + "的关联吗？"))
				{
					var myForm = document.getElementById(formId);
					myForm.action = url;
					myForm.submit();
				}
			}
			else
				alert(ippool[i].value + "未分配且未和任何虚拟机实例绑定！");
			return;
		}
	}
	alert("请选择取消关联的IP地址！");
}

function ippool_associate_state(formId)
{
	var instance = document.getElementById("instanceId");
	var instanceFields = instance.value.split(" ");
	if (instanceFields[1] == "running")
	{
		var myForm = document.getElementById(formId);
		myForm.submit();
	}
	else
		alert("实例状态不是running，不能关联！");
}
