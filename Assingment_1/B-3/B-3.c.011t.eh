
;; Function main (main, funcdef_no=23, decl_uid=2510, cgraph_uid=24, symbol_order=23)

main ()
{
  int b;
  int a;
  int D.2521;

  a = 4;
  goto <D.2515>;
  <D.2514>:
  if (a <= 3) goto <D.2518>; else goto <D.2519>;
  <D.2518>:
  b = b + 2;
  goto <D.2520>;
  <D.2519>:
  b = b * 2;
  <D.2520>:
  a = a + 1;
  <D.2515>:
  if (a <= 99) goto <D.2514>; else goto <D.2516>;
  <D.2516>:
  printf ("%d%d", a, b);
  D.2521 = 0;
  goto <D.2522>;
  <D.2522>:
  return D.2521;
}



;; Function printf (<unset-asm-name>, funcdef_no=15, decl_uid=937, cgraph_uid=16, symbol_order=15)

__attribute__((artificial, gnu_inline, always_inline))
printf (const char * restrict __fmt)
{
  int D.2523;

  D.2523 = __printf_chk (1, __fmt, __builtin_va_arg_pack ());
  goto <D.2524>;
  <D.2524>:
  return D.2523;
}


