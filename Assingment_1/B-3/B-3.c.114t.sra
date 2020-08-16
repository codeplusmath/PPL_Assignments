
;; Function main (main, funcdef_no=23, decl_uid=2510, cgraph_uid=24, symbol_order=23) (executed once)

main ()
{
  int b;
  int a;

  <bb 2> [local count: 11059540]:

  <bb 3> [local count: 1062682284]:
  # a_12 = PHI <4(2), a_6(5)>
  # b_13 = PHI <b_3(D)(2), b_5(5)>
  b_5 = b_13 * 2;
  a_6 = a_12 + 1;
  if (a_6 != 100)
    goto <bb 5>; [98.96%]
  else
    goto <bb 4>; [1.04%]

  <bb 5> [local count: 1051622743]:
  goto <bb 3>; [100.00%]

  <bb 4> [local count: 11059541]:
  __printf_chk (1, "%d%d", 100, b_5);
  return 0;

}


