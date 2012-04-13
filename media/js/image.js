var MainSel  = null;
var SlaveSel = null;

//MainSel  = document.getElementById("select1");
//SlaveSel = document.getElementById("select2");
//alert('MainSel'+MainSel);
function DoAdd()
{
	for (var i = 0;i < MainSel.options.length; i++)
	{
		var flag = 0;
		if (MainSel.options[i].selected == true)
		{
			for (var j = 0; j < SlaveSel.options.length; j++)
				if (MainSel.options[i].value == SlaveSel.options[j].value)
				{	 
					flag = 1;
					break;
				}		
			if (flag == 0)
				SlaveSel.options.add(new Option(MainSel[i].text, MainSel[i].value));			
		}
	}
}

function DoDel()
{
	for(var i = SlaveSel.options.length - 1; i >= 0; i--)
	{
		if (SlaveSel.options[i].selected == true)
			SlaveSel.remove(i);
	}
}

function image_start(cbname, formId, url)
{
	var image = document.getElementsByName(cbname);
	for (var i = 0; i < image.length; i++)
	{
		if (image[i].checked)
		{
			valueFields = image[i].value.split(' ');
			if (valueFields[3] == "available")
			{
				if (confirm("确定要启动此镜像吗？"))
				{
					var myForm = document.getElementById(formId);
					myForm.action = url;
					myForm.submit();
				}
			}
			else
				alert("此状态下禁止启动！");
			return;
		}
	}
	alert("请选要择启动的镜像！");
}

function image_checkout(cbname, formId, url)
{
	var image = document.getElementsByName(cbname);
	for (var i = 0; i < image.length; i++)
	{
		if (image[i].checked)
		{
			if (confirm("确定要注销此镜像吗？"))
			{
				var myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			return;
		}
	}
	alert("请选择要注销的镜像！");
}

function check_file(eki_file, eri_file, emi_file, formid, url, o1, o2)
{
	var eki = document.getElementById(eki_file);
	var eri = document.getElementById(eri_file);
	var emi = document.getElementById(emi_file);
	if (eki.value == "" || eri.value == "" || emi.value == "")
		alert("请点击浏览按钮，选择您要上传的镜像文件！");
	else
	{
        var o1 = document.getElementById(o1); 
	    var o2 = document.getElementById(o2); 
		o1.style.width = document.documentElement.scrollWidth; 
		o1.style.height = document.documentElement.scrollHeight; 
		o1.style.display = "block"; 
		o2.style.display = "block";

        var myForm = document.getElementById(formid);
		myForm.action = url;
		myForm.submit();
	}
}

function register_image(eki_file, eri_file, emi_file, imgType, formId, url, o1, o2)
{
	var imageType = document.getElementsByName(imgType)
	for (var i = 0; i < imageType.length; i++)
	{
		if (imageType[i].checked)
		{
			var eki = document.getElementById(eki_file);
			var eri = document.getElementById(eri_file);
			var emi = document.getElementById(emi_file);
			if (eki.value == "" || eri.value == "" || emi.value == "")
				alert("请点击浏览按钮，选择您要上传的镜像文件！");
			else
			{
				var o1 = document.getElementById(o1);
				var o2 = document.getElementById(o2);
				o1.style.width = document.documentElement.scrollWidth;
				o1.style.height = document.documentElement.scrollHeight;
				o1.style.display = "block";
				o2.style.display = "block";

				var myForm=document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			return;
		}
	}
	alert("请选择镜像类型！");
}

function check_ami(ami_file, formId, url)
{
	var ami = document.getElementById(ami_file);
	if (ami.value)
	{
		var myForm = document.getElementById(formId);
		myForm.action = url;
		myForm.submit();
		return;
	}
	alert("请点击浏览按钮，选择您要上传的 manifest 文件！");
}

function del_image(select_file, formId, url)
{
    var select = document.getElementById(select_file);
    for (var i = 0; i < select.options.length; i++)
    {
        if (select.options[i].selected)
        {
			if (confirm("确定要删除镜像吗？"))
			{
				var myForm = document.getElementById(formId);
				myForm.action = url;
				myForm.submit();
			}
			return;
        }
    }
	alert("请选择要删除的镜像！");
}

function file_add(select1, file)
{
	var sel = document.getElementById(select1);
	for (var i = 0;i < sel.options.length; i++)
	{
		var flag = 0;
        if (sel.options[i].selected)
        {
			var sel_file = document.getElementById(file);
			sel_file.value = sel[i].text;
			return;
		}
	}
}

function file_del(file)
{
	var sel_file = document.getElementById(file);
	sel_file.value = "";

}
