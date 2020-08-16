
;; Function main (main, funcdef_no=23, decl_uid=2511, cgraph_uid=24, symbol_order=24)

main ()
{
  int a;
  int i;
  int D.2519;

  a = 10;
  i = 0;
  goto <D.2516>;
  <D.2515>:
  a = a + 1;
  i = i + 1;
  <D.2516>:
  if (i <= 3) goto <D.2515>; else goto <D.2517>;
  <D.2517>:
  printf ("%d", a);
  D.2519 = a;
  goto <D.2520>;
  D.2519 = 0;
  goto <D.2520>;
  <D.2520>:
  return D.2519;
}



;; Function printf (<unset-asm-name>, funcdef_no=15, decl_uid=937, cgraph_uid=16, symbol_order=15)

__attribute__((artificial, gnu_inline, always_inline))
printf (const char * restrict __fmt)
{
  int D.2521;

  D.2521 = __printf_chk (1, __fmt, __builtin_va_arg_pack ());
  goto <D.2522>;
  <D.2522>:
  return D.2521;
}


