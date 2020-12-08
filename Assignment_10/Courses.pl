teaches_subject(t1,math).
teaches_subject(t2,ppl).
teaches_subject(t3,dsa).
teaches_subject(t4,dld).
teaches_subject(t5,ppl).
teaches_subject(t6,dtl).
teaches_subject(t7,dsa).

has_subject(math_dept,math).
has_subject(comp_dept,dsa).
has_subject(comp_dept,ppl).
has_subject(comp_dept,dtl).
has_subject(comp_dept,dld).

has_student(comp_dept,s1).
has_student(comp_dept,s2).
has_student(comp_dept,s3).
has_student(comp_dept,s4).
has_student(comp_dept,s5).

div(s1,div1).
div(s2,div2).
div(s3,div1).
div(s4,div2).
div(s5,div1).
div(t2,div1).
div(t5,div2).
div(t3,div1).
div(t7,div2).


taught_dsa_by(D,F) :- div(F,D) , teaches_subject(F,dsa).
taught_ppl_by(D,F) :- div(F,D) , teaches_subject(F,ppl).
has_faculty(D,F) :- teaches_subject(F,S) , has_subject(D,S).
studies_subject(ST,SB) :- has_student(D,ST) , has_subject(D,SB).
studies_under(S,F) :- has_subject(D,SB) , has_student(D,S) , teaches_subject(F,SB).
