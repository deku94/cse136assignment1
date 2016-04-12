#!/usr/bin/perl -wT
use CGI qw(:standard);

print header;
print start_html("Form Result");
print "<h1 align='center'>Form Result</h1><hr>";

my %form;
foreach my $p (param()) {
   $form{$p} = param($p);
   print "$p = $form{$p}<br>";
}
print end_html;
