function CheckTitle(myCheck, checkId)
{
    var checkAll = document.getElementsByName(myCheck);
    var checkTitle = document.getElementById(checkId);
    for (var i = 0; i < checkAll.length; i++)
        checkAll[i].checked = checkTitle.checked;
}
function check(myCheck, checkId)
{
    var checkAll = document.getElementsByName(myCheck);
    var checkTitle = document.getElementById(checkId);
    var checklen = $("input[name='cb']:checked").length;
    if (checklen != checkAll.length)
      checkTitle.checked = false;
    if (checklen == checkAll.length)
      checkTitle.checked = true;
}

function del_members(submitform,url) {
    var submitform = document.getElementById(submitform);
    var myCheck = document.getElementsByName('cb');
    var checkAll = document.getElementById('checkall');
    var hasChecked=false;
    for(var i=0;i<myCheck.length;i++)
    {
        if(myCheck[i].checked == true)
        {
            hasChecked = true;
            break;
        }
    }
    if(checkAll.checked == true)
        hasChecked = true;
    if(hasChecked == false) {
        alert('请选择要删除的数据！');
    }else if(confirm("确定要删除？")) 
        {
		submitform.action = url;
                submitform.submit();
        }
   }
   
   function editor_members(submitform,url) {
    var submitform = document.getElementById(submitform);
    var myCheck = document.getElementsByName('cb');
    var hasChecked=false;
    if (myCheck.length > 1 || myCheck.length < 0)
        alert("只能选择一天数据进行修改!");
    else
    {
        if(myCheck[0].checked == true)
        {
            hasChecked = true;
        }
    }
    if(hasChecked == false) {
        alert('请选择要修改的数据！');
    }else{
		submitform.action = url;
                submitform.submit();
        }
   }