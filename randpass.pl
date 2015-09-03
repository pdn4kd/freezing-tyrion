#! /usr/bin/perl
use strict;
use warnings;

# A toy password generator. Outputs a string of the specified length containing a combination of the 95 printable ASCII characters. Well, far fewer in the inital versions. (no spaces)

my @randchars = qw/ ` 1 2 3 4 5 6 7 8 9 0 - = q w e r t y u i o p [ ] \ a s d f g h j k l ; ' z x c v b n m . \/ _ + ~ ! @ $ % ^ & * ( ) Q W E R T Y U I O P { } | A S D F G H J K L : " Z X C V B N M < > ? /;
print $randchars[90];

if (defined($ARGV[0]) && ($#ARGV + 1 < 2) && ($ARGV[0] < 33) && ($ARGV[0] > 0)) {
	foreach (0 .. $ARGV[0]) {
		my $foo = int(rand(@randchars));
		print($randchars[$foo]);
	}
	print "\n";

} else {
	print "Random password generator. Invoke with a number (1-32) to generate a password of that length containing a random combination of printable ASCII characters. (".@randchars."/95 available -- no commas, octothorps, or spaces)\n";
}
