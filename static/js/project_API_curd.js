

var url;
function newProjectAPI(){
    var project_id = document.getElementById("project_id_flag").value;
           // alert(project_id);
    url = '/AutoFW/startAPI/'+project_id;
//            alert('newUser:'+url);
    $('#dlg').dialog('open').dialog('center').dialog('创建','New Project API');
    $('#fm').form('clear');
}


// 创建——API 并 SAVE  保存
function saveProjectAPI(username){
            // alert('saveUser:'+url+username);
   $('#fm').form('submit',{
        url: url+'/'+username,
        onSubmit: function(){
            return $(this).form('validate');
        },
        success: function(result){
            if (result=="save"){
               $('#dlg').dialog('close');
                $('#dg_case').datagrid('reload');
            }else
            if (result.errorMsg){
                $.messager.show({
                    title: 'Error',
                    msg: result.errorMsg
                });
            }
            else {
                $('#dlg').dialog('close');        // close the dialog
                $('#dg_case').datagrid('reload');    // reload the user data
            }
        }
    });
}


//修改接口
function editProjectAPI(){
    // $('#fm_case_id').attr("disabled","disabled"); //???未生效

    var project_id = document.getElementById("project_id_flag").value;
    var row = $('#dg_case').datagrid('getSelected');

    if(row){
        $('#dlg').dialog('open').dialog('center').dialog('setTitle','Edit Project API');
        $('#fm').form('load',row);
        url = '/AutoFW/editAPI/'+project_id;
    }

}


//删除API
function deleteProjectAPI(){
    var row = $('#dg_case').datagrid('getSelected');
    var data = JSON.stringify(row)
    $.messager.confirm('Confirm','Are you sure you want to destroy this module?',function(r){
      if (r){
          $.ajax({
            url: '/AutoFW/removeAPI/',
            type: 'POST',
            data: {id:row.case_id},
            success: function(data) {
                if (data=="REMOVE"){
                    $('#dg_case').datagrid('reload');    // reload the user data bug
                }
            },
            error: function(data) {alert("error")}
         });
      }
    });
}