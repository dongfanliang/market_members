function CheckItem(myCheck, checkid) {
    var checkAll = document.getElementById( checkid );
    var checkItems = document.getElementsByName( myCheck );
    var check_status = 0;
    for (var i =0; i < checkItems.length; i++) {
          if(checkItems[i].checked == false){
              check_status = 0;
              break;
	}
        else
             check_status ++;
    }
   if(check_status == 0)
            checkAll.checked = false;
   else 
            checkAll.checked = true;
}
function CheckTitle(myCheck,checkid) {
    var checkAll = document.getElementsByName( myCheck );
    var checkTitle = document.getElementById( checkid );
    for (var i = 0; i < checkAll.length; i++) {
        checkAll[i].checked = checkTitle.checked;
    }
}
//----------connect js ----------------- 
function judg_conn(url)
{
	var input1 = document.getElementById("id_acc");
	var input2 = document.getElementById("id_sec");
	if (!(input1.value && input2.value))
	{	alert("请输入需要填写的内容！");
	}
	else
	{
		var myform = document.getElementById("connform");
		myform.action = url;
		myform.submit();
	}
	
}
function save_conn_name(url)
{
	var input0 = document.getElementById("Input");
	var input1 = document.getElementById("Input2");
	var input2 = document.getElementById("passId");
	if (!(input0.value && input1.value && input2.value ))
	{
		alert("输入所有内容后才能够保存，请填写完整！");
	}
	else
	{
		var myform = document.getElementById("connform");
		myform.action = url;
		myform.submit();
	}


}
//-------------connect end------------------
function submit_form(formid,url)
{
	var myform = document.getElementById(formid);
	myform.action = url;
	myform.submit();
}
function deleteuser(id,formid,url)
{
	var count=0;
	var namebox=document.getElementsByName(id);
	for(var i=0; i<namebox.length; i++ )
	{
		if ( namebox[i].checked )
		{
			count=count+1;
			break;
		}
	}
	if (count ==0 )
	{
		alert("请选择要删除的内容！");
	}
	else
	{
		if( confirm( "确定要删除么？" ))
		{
			var myform=document.getElementById(formid);
			myform.action=url;
			myform.submit();
		}
		else
		{
			return;
		}
	}
}

function DelData(submitform, checkMessage) {
    var submitform = document.getElementById(submitform);
    var myCheck = document.getElementsByName(checkMessage);
    var hasChecked=false;
    for(var i=0;i<myCheck.length;i++)
    {
        if(myCheck[i].checked==true)
        {
            hasChecked=true;
            break;
        }
    }
    if (hasChecked == false) {
        alert('请选择要删除的数据！');
    }
    else
        if (confirm("确定要删除？")) {
        submitform.submit();
    }
}


function isNumber(str) {
    var patrn = /^\d{1,8}$/;
    if (patrn.exec(str)) {
        return true;
    }
    else {
        return false;
    }
}

function isAllNumber(str) {
    var patrn = /^\d+$/;
    if (patrn.exec(str)) {
        return true;
    }
    else {
        return false;
    }
}

function isIDNumber(str)
{
    var patrn=/^\d{15}$|^\d{18}$/;
    if(patrn.exec(str))
    {
    	return true;
    }
    else
    {
    return false;
    }
}

function isPhoneNumber(str)
{
	var patrn1=/^\d{7,8}$/;
	var patrn2=/^\(0[1-9]{2,3}\)\d{7,8}$/;
	var patrn3=/^0[1-9]{2,3}-\d{7,8}$/;
	var patrn4=/^\d{11,12}$/;
    if(patrn1.exec(str)||patrn2.exec(str)||patrn3.exec(str)||patrn4.exec(str))
    {
    	return true;
    }else{
        return false;
    }
}
function isMobilePhoneNumber(str)
{
	var patrn=/^\d{11,12}$/;
    if(patrn.exec(str))
    {
    	return true;
    }
    else
    {
        return false;
    }
}

function isEmail(str)
{
	var patrn=/^\w+@\w+\.\w+$/;
    if(patrn.exec(str))
    {
    	return true;
    }
    else
    {
        return false;
    }
}


//具体验证内容

    function validateMobilePhoneNumber(obj)
    {
        if(obj.value.length>0){
            if(!(isMobilePhoneNumber(obj.value))){
                alert("手机号码格式不正确，请重新输入！");
                obj.value="";
            }
        }
    }
    function validatePhoneNumber(obj){
        if(obj.value.length>0){
            if(!(isPhoneNumber(obj.value))){
                alert("电话号码格式不正确，请重新输入！");
                obj.value="";
            }
        }
    }
    function validateEmail(obj){
        if(obj.value.length>0){
            if(!(isEmail(obj.value))){
                alert("邮箱格式不正确！");
                obj.value="";
            }
        }
    }
    function validateIDNumber(obj){
        if(obj.value.length>0){
            if(!(isIDNumber(obj.value))){
                alert("身份证号码格式不正确！");
                obj.value="";
            }
        }
    }
	function stopInstance(instanceID, formInstance, url)
	{
		var count = 0;
		var namebox = document.getElementsByName(instanceID);
		for (var i = 0; i < namebox.length; i++)
		{
			if(namebox[i].checked)
			{
				count++;
			}
		}
		if( count == 0 )
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
function validate_VolumeAttach(thisform) {
   var inst_id = document.getElementById('instance_id');
   var device = document.getElementById('id_device');
   if( device.value == ""){
       alert("请输入device！");
       return false;
   }
   else{
   if( inst_id.value == "none") {
       alert("请选择一个实例！");
       return false;
   }
   else{
       thisform.submit();
}
}
}
function detach_Volume(vol_id, vol_status,vol_attach) {
   
    if(vol_status != 'in-use'){
       alert("该volume未与任何实例进行绑定！");
       return false;
    }
    else{
         if(vol_attach == "attached")
         {   
              msg = vol_id + "正在使用！是否确定移除绑定？"
              if(confirm(msg))
                window.location = "/volumedetach/?vol_id="+ vol_id;
         }

         if(vol_attach == "detaching")
         {
              msg = vol_id + "正在移除绑定中禁止再次移除，请刷新后查看状态继续操作！";
              alert(msg);
         }
         if(vol_attach == "attaching")
         {
              msg = "绑定中禁止移除！请刷新查看最新状态后操作！";
              alert(msg);
         }
         else
              return false;
    }
  }

function validate_Volume(thisform) {
   var zone = document.getElementById('avail_zone');
   var size = document.getElementById('id_size');
   if( size.value == ""){
       alert("请输入 volume的大小！");
       return false;
   }
   else if( size.value <=0 || size.value > 1024)
   {
       alert("输入的大小不符合要求，请重新输入！");
       return false;
   }
   else{
   	if( zone.value == "none") {
       	alert("请选择一个可用域！");
       	return false;
   	}
   	else{
       	thisform.submit();

}
}
}

function GoPage(page, range, url) {
   var p = document.getElementById(page);
   if( p.value == "")
   {
      alert("请输入要跳转的页码！");
      return false;
   }
   else{
      var reg = /^\d+$/;
     if(reg.test(p.value) == false ){  
       alert("输入有误！");
       return false;
     }
     else {
	 if( p.value <=0 || p.value > range)
   	{
	      alert("错误的页码！");
      	      return false;
   	}
   	else
     	 window.location = url + '?page=' + p.value;
    }
}
}
function validate_snapshot(thisform) {
   var zone = document.getElementById('avail_zone');
   var volume = document.getElementById('volume_id');
   if( volume.value == "none") {
       alert("请选择一个Volume！");
       return false;
   }
   else{
       if( zone.value == "none") {
           alert("请选择一个可用域！");
           return false;
        }
        else
           thisform.submit();
  }
}


function del_Volume(submitform) {
    var submitform = document.getElementById(submitform);
    var myCheck = document.getElementsByName('checkbox');
    var checkAll = document.getElementById('checkall');
    var hasChecked=false;
    for(var i=0;i<myCheck.length;i++)
    {
        if(myCheck[i].checked==true)
        {
            hasChecked=true;
            break;
        }
    }
    if(checkAll.checked == true)
         hsChecked=true;
    if (hasChecked == false) {
        alert('请选择要删除的数据！');
    }
    else
    {
	var valueArray = myCheck[i].value.split(" ");
	if (valueArray[1] == "creating")
	{
		var meg = "逻辑卷" + valueArray[0] + "正在创建，不能删除！";
                alert(meg);
                return false;
	}
	if(myCheck[i].id == 'attached')
                {
                var meg = "请先移除"+ valueArray[0] +"的绑定！";
                alert(meg);
                return false;
                }
        if(myCheck[i].id == 'attaching')
                {
                var meg = "正在绑定中，请点击刷新根据相应状态进行操作！";
                alert(meg);
                return false;
                }
        if (confirm("确定要删除？")) 
        {
        alert("稍等片刻后刷新，逻辑卷状态变为deleted再次刷新即可删除！");
        submitform.submit();
        }
   }
}
function del_Snapshot(thisform){
    var submitform = document.getElementById(thisform);
    var myCheck = document.getElementsByName('checkbox');
    var checkAll = document.getElementById('checkall');
    var hasChecked=false;
	var haspending = false;
    for(var i=0;i<myCheck.length;i++)
    {
        if(myCheck[i].checked==true)
        {
            hasChecked=true;
			if (myCheck[i].id == 'pending')
				haspending = true;
				break;
        }
    }
    if (hasChecked == false) {
        alert("请选择要删除的数据！");
        return false;
     }
    else{
        if (haspending == true)
			alert("选择的快照中有正在启动的快照，无法删除。");
        else
            if(confirm("确定要删除？"))
                submitform.submit();
    }


}
function expan_Volume(formid, url)
{
	var myCheck = document.getElementsByName('checkbox');
	var count = 0;
	var checked = 0;
	for(var i=0;i<myCheck.length;i++)
	{
		if(myCheck[i].checked==true)
 		{
			count ++;
			checked = i;
		}
		if (count >1 )
		{
			break;
		}
	}
	if (count == 1)
	{
		var myform = document.getElementById(formid);
		value = myCheck[checked].value.split(' ');
		myform.action = url + value[0] + '/';
		myform.submit();
	}else alert('请选择一个逻辑卷进行扩容！');
}

function getSelectedItem(){ 
 var arr = document.getElementsByName('checkbox'); 
 for(var n=0;n <arr.length;n++){
  if(arr[n].checked) 
	self.location='/volume/?id='+arr[n].value;

} 
}

