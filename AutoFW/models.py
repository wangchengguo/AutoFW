#coding=utf-8
from django.db import models


#用户信息
class UserInfo(models.Model):
    id = models.IntegerField
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=100)
    authority = models.CharField(max_length=20)#super/common/guest
    createtime = models.DateTimeField()
    remark = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)

    class Meta:
        db_table = 'userinfo'


#项目信息
class Project(models.Model):
    id = models.IntegerField
    project_code = models.CharField(max_length=20,unique=True)
    project_name = models.CharField(max_length=50,unique=True)
    PRI = models.CharField(max_length=10)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=20)
    department = models.CharField(max_length=30)

    class Meta:
        db_table = 'project'


# 项目全局设置
class Project_Config(models.Model):
    project_id = models.ForeignKey(Project, to_field="project_code")
    ip = models.CharField(max_length=30, primary_key=True)
    domain = models.CharField(max_length=200)
    port = models.IntegerField()
    protocol = models.CharField(max_length=100)
    bak_field2 = models.CharField(max_length=100)

    class Meta:
        db_table = 'project_config'


#项目模块信息
class Project_Module(models.Model):
    project = models.ForeignKey(Project,to_field="project_code")
    module_id = models.CharField(max_length=20)
    module_name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = 'project_module'


#接口信息
class Project_Case(models.Model):
    case_id = models.CharField(max_length=30,primary_key=True)
    module_name = models.ForeignKey(Project_Module,to_field="module_name")
    project_name = models.ForeignKey(Project,to_field="project_name")
    case_name = models.CharField(max_length=30,unique=True)
    creator = models.CharField(max_length=20)
    url_path = models.CharField(max_length=150)
    port = models.IntegerField
    method = models.CharField(max_length=20)
    parameter_format = models.CharField(max_length=50,null=True)
    parameter = models.CharField(max_length=1500)
    expected = models.CharField(max_length=300)
    description = models.CharField(max_length=100)
    headers = models.CharField(max_length=1000)

    class Meta:
        db_table = 'project_case'


#成员信息（使用该系统的成员）
class Emp_Info(models.Model):
    user_id =models.ForeignKey(UserInfo,to_field="username")
    name = models.CharField(max_length=20)
    birthday = models.DateTimeField()
    email = models.CharField(max_length=50,unique=True)
    phone_id = models.CharField(max_length=11)
    position = models.CharField(max_length=30)
    salery = models.IntegerField()
    work_year = models.IntegerField()
    remark = models.CharField(max_length=50)
    job_number = models.IntegerField(primary_key=True)
    other = models.CharField(max_length=30)

    class Meta:
        db_table = 'emp_info'


#生成的脚本信息
class Script_Info(models.Model):
    script_name = models.CharField(max_length=100,primary_key=True)
    script_path = models.CharField(max_length=200)
    script_case_name = models.ForeignKey(Project_Case,to_field="case_name")
    create_time = models.CharField(max_length=30)
    script_module_name = models.ForeignKey(Project_Module,to_field="module_name")
    script_status = models.CharField(max_length=30)
    script_project_name = models.ForeignKey(Project,to_field="project_name")
    remark = models.CharField(max_length=40)

    class Meta:
        db_table = 'script_info'


#批次执行测试脚本生成数据信息表
class Batch_Report(models.Model):
    report_id = models.CharField(max_length=50,unique=True)
    report_name = models.CharField(max_length=100,primary_key=True)
    API_total = models.IntegerField(null=False)
    pass_total = models.IntegerField()
    fail_total = models.IntegerField()
    skip_total = models.IntegerField()
    execute_man = models.CharField(max_length=30)
    # API_name = models.CharField(max_length=100,default=None)
    # execute_log = models.CharField(max_length=1500)
    execute_time = models.DateTimeField()
    bak1 = models.CharField(max_length=50)
    bak2 = models.CharField(max_length=50)


    class Meta:
        db_table = 'batch_report'


class Execute_Script_Log(models.Model):
    log_report_id = models.ForeignKey(Batch_Report,to_field="report_id")
    log_api_name = models.CharField(max_length=100,null=False)
    log_execute_script = models.CharField(max_length=3000)
    bak1 = models.CharField(max_length=50)
    # bak2 = models.CharField(max_length=50)
    # bak3 = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default=None)

    class Meta:
        db_table = 'execute_script_log'