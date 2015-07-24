#! usr/bin/perl
use strict;
use warnings;
use Text::CSV;

open my $input0, "<", "BSPH.csv" or die "cannot open BSPH.csv: $!";
open my $output0, ">", "BRSPHmatchlines461czd.csv" or die "cannot open BRSPHmatch.csv: $!";
print $output0 "BSPHnyuID,RSPHnyuID\r\n";
open my $output1, ">", "BRSPHmatchcount461czd.csv" or die "cannot open BRSPHmatchcount.csv: $!";
print $output1 "nyuID,matches\r\n";

my $csv0 = Text::CSV->new({ binary => 1 });
$csv0->column_names( $csv0->getline($input0));
while (my $row = $csv0->getline_hr($input0)) {
	open my $input1, "<", "RSPHdownselect.csv" or die "cannot open RSPHdownselect.csv: $!";
	my $csv1 = Text::CSV->new({ binary => 1 });
	$csv1->column_names( $csv1->getline($input1));
	my $match_count = 0;
	my $nyuID = $row->{nyuID};
	my $z = $row->{zgal};
	my $mstar = $row->{'logMstar(Msun/h2)'};
	my $mhalo = $row->{'logMhalo2(Msun/h)'};
	my $rank = $row->{rank2};
	while (my $row1 = $csv1->getline_hr($input1)) {
		if ((abs($z - $row1->{zgal}) <= 0.01) && (abs($mstar - $row1->{'logMstar(Msun/h2)'}) <= 0.4) && (abs($mhalo - $row1->{'logMhalo2(Msun/h)'}) <= 0.6) && ($rank == $row1->{rank2})) {
			print $output0 ($nyuID . "," . $row1->{nyuID} . "\r\n");
			$match_count += 1;
		}
	}
	close $input1;
	print $output1 ($nyuID . "," . $match_count . "\r\n");
}
close $input0;
close $output0;
close $output1;
