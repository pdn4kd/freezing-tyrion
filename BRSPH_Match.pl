#!/usr/bin/perl
use strict;
use warnings;
use Text::CSV;

#matching script for finding red spheroids to complement our blue spheroids. Hilariously inefficient, because I don't know how to parse CSVs.

open my $input0, '<', "BSPH.csv" or die "cannot open BSPH.csv: $!";
my $csv0 = Text::CSV->new({ binary => 1 });
$csv0->column_names( $csv0->getline($input0) );

#open my $input1, '<', "RSPH.csv" or die "cannot open BSPH.csv: $!";
#my $csv1 = Text::CSV->new({ binary => 1 });
#$csv1->column_names( $csv1->getline($input1) );

open my $output, '>', "BR_matches.csv" or die "cannot open BR_matches.csv: $!";

while (my $row0 = $csv0->getline_hr($input0)) {
	#wrong, but since I'm not sure how to reset the cycle through $csv1, just reopening the file.
	open my $input1, '<', "RSPH.csv" or die "cannot open BSPH.csv: $!";
	my $csv1 = Text::CSV->new({ binary => 1 });
	$csv1->column_names( $csv1->getline($input1) );
	while (my $row1 = $csv1->getline_hr($input1)) {
		if ((abs($row0->{conc_r} - $row1->{conc_r}) <= 0.05) && (abs($row0->{zgal} - $row1->{zgal}) <= 0.05) && (abs($row0->{logMstar} - $row1->{logMstar}) <= 0.05)) {
			print $output "$row0->{nyuID}, $row1->{nyuID}\r\n";
		}
	}
}

