from peewee import *
from utils.codes import *

database = PostgresqlDatabase('ria', **{'user': 'postgres'})


answer_yes_no = {
    ("Y", "Y"),
    ("N", "N")
}


class BaseModel(Model):
    class Meta:
        database = database


class IAPDReport(BaseModel):
    gen_on = DateTimeField()
    # indvl = ForeignKeyField()

    class Meta:
        db_table = 'iapdreport'


class Indvl(BaseModel):
    iapd_report = ForeignKeyField(IAPDReport, related_name='indvls')

    class Meta:
        db_table = 'indvl'


class CrntEmp(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='crnt_emps')
    org_nm = CharField(max_length=64)
    org_pk = IntegerField()
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'crntemp'


class BrnchOfLoc(BaseModel):
    crnt_emp = ForeignKeyField(CrntEmp, related_name='brnch_of_locs')
    prev_rgstns = ForeignKeyField(PrevRgstn, related_name='brnch_of_locs')
    city = CharField(null=True, max_length=50)
    cntry = CharField(null=True, max_length=50)
    postl_cd = CharField(null=True, max_length=11)
    state = CharField(null=True, choices=state_code)
    str1 = CharField(null=True, max_length=50)
    str2 = CharField(null=True, max_length=50)

    class Meta:
        db_table = 'brnchofloc'


class CrntRgstn(BaseModel):
    crnt_emp = ForeignKeyField(CrntEmp, related_name='crnt_rgstns')
    reg_auth = CharField(choices=state_code)
    reg_cat = CharField(choices=registration_category)
    st = CharField(choices=registration_status)
    st_dt = DateTimeField()

    class Meta:
        db_table = 'crntrgstn'


class DRP(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='drps')
    has_reg_action = CharField(null=True, choices=answer_yes_no)
    has_criminal = CharField(null=True, choices=answer_yes_no)
    has_bankrupt = CharField(null=True, choices=answer_yes_no)
    has_civil_judc = CharField(null=True, choices=answer_yes_no)
    has_bond = CharField(null=True, choices=answer_yes_no)
    has_judgment = CharField(null=True, choices=answer_yes_no)
    has_invstgn = CharField(null=True, choices=answer_yes_no)
    has_cust_comp = CharField(null=True, choices=answer_yes_no)
    has_termination = CharField(null=True, choices=answer_yes_no)

    class Meta:
        db_table = 'drp'


class Dsgntn(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='dsgntns')
    dsgntn_nm = CharField(max_length=128)

    class Meta:
        db_table = 'dsgntn'


class EmpHist(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='emp_hss')
    from_dt = CharField(max_length=7)
    to_dt = CharField(max_length=7)
    org_nm = CharField(max_length=64)
    city = CharField(max_length=50)
    state = CharField(null=True, choices=state_code)

    class Meta:
        db_table = 'emphist'


class Exm(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='exms')
    exm_cd = CharField(choices=exam_code)
    exm_dt = DateTimeField(null=True)
    exm_nm = CharField(max_length=128)

    class Meta:
        db_table = 'exm'


class Info(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='info')
    actv_ag_reg = CharField(null=True, choices=answer_yes_no)
    indvlp_k = IntegerField()
    link = CharField(null=True, max_length=128)
    first_nm = CharField(null=True, max_length=25)
    last_nm = CharField(null=True, max_length=25)
    mid_nm = CharField(null=True, max_length=20)
    suf_nm = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'info'


# complete
class OthrBus(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='othr_buss')
    desc = CharField(max_length=4000)

    class Meta:
        db_table = 'othrbus'


class OthrNm(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='othr_nms')
    first_nm = CharField(null=True, max_length=25)
    last_nm = CharField(null=True, max_length=25)
    mid_nm = CharField(null=True, max_length=20)
    suf_nm = CharField(null=True, max_length=5)

    class Meta:
        db_table = 'othrnm'


class PrevRgstn(BaseModel):
    indvl = ForeignKeyField(Indvl, related_name='prev_rgstns')
    iapd_report = ForeignKeyField(IAPDReport, related_name='prev_rgstns')
    org_nm = CharField(max_length=64)
    org_pk = IntegerField()
    reg_begin_dt = DateTimeField(null=True)
    reg_end_dt = DateTimeField(null=True)

    class Meta:
        db_table = 'prevrgstn'
