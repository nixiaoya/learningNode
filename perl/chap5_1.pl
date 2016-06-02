#!/bin/env perl
#倒序输入文本内容

@list = <>;
@argv = reverse @list;
print @argv;
