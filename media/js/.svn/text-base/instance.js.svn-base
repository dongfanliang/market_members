function stopInstance(cbname, formId, url)
{
	var instance = document.getElementsByName(cbname);
	for (var i = 0; i < instance.length; i++)
	{
		if (instance[i].checked)
		{
			var instanceFields = instance[i].value.split(' ');
			if (instanceFields[6] == "running")
			{
				myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			else
				alert("选择的虚拟机实例不是running状态，无法注销！");
			return;
		}
	}
	alert("请选择要注销的实例！");
}

function shutdownInstance(cbname, formId, url)
{
	var instance = document.getElementsByName(cbname);
	for (var i = 0; i < instance.length; i++)
	{
		if (instance[i].checked)
		{
			var instanceFields = instance[i].value.split(' ');
			if (instanceFields[6] == "running")
			{
				myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			else
				alert("选择的虚拟机实例不是running状态，无法关闭！");
			return;
		}
	}
	alert("请选择要关闭的实例！");
}

function startInstance(cbname, formId, url)
{
	var instance = document.getElementsByName(cbname);
	for (var i = 0; i < instance.length; i++)
	{
		if (instance[i].checked)
		{
			var instanceFields = instance[i].value.split(' ');
			if (instanceFields[6] == "shutteddown")
			{
				myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			else
				alert("选择的虚拟机实例不是shutteddown状态，无法启动！");
			return;
		}
	}
	alert("请选择要启动的实例！");
}

function restartInstance(cbname, formId, url)
{
    var instance = document.getElementsByName(cbname);
    for (var i = 0; i < instance.length; i++)
    {
        if (instance[i].checked)
        {
                myForm = document.getElementById(formId);
                myForm.action = url;
                myForm.submit();
            return;
        }
    }
    alert("请选择要重启的实例！");
}

function migrateInstance(cbname, formId, url)
{
	var instance = document.getElementsByName(cbname);
	var instanceFields = instance[0].value.split(' ');
	if (instanceFields[1] == "running")
	{
		myForm = document.getElementById(formId);
		myForm.action = url;
		myForm.submit();
	}
	else
		alert("选择的虚拟机实例不是running状态，无法迁移！");
}

function fileOpen()
{
	var file = document.getElementById("fileId");
	file.click();
	var str = s.value;
}
