#! usr/bin/perl
use strict;
use warnings;
use Text::CSV;

open my $BSPHin, "<", "BSPH.csv" or die "cannot open BSPH.csv: $!";
my $csv0 = Text::CSV->new({ binary => 1 });
$csv0->column_names( $csv0->getline($BSPHin));
open my $output0, ">", "BRSPHmatchlinesc.csv" or die "cannot open BRSPHmatch.csv: $!";
print $output0 "BSPHnyuID,RSPHnyuID\r\n";
open my $output1, ">", "BRSPHmatchcountc.csv" or die "cannot open BRSPHmatchcount.csv: $!";
print $output1 "nyuID,matches\r\n";

open my $RSPHin, "<", "RSPH.csv" or die "cannot open RSPH.csv: $!";
my $csv1 = Text::CSV->new({ binary => 1 });
# map RSPH info to arrays
$csv1->column_names( $csv1->getline($RSPHin));
my $RSPHval = $csv1->getline_hr_all($RSPHin);
my @nyuIDR = map {$_->{'nyuID'}} @{$RSPHval};
my @zR = map {$_->{'zgal'}} @{$RSPHval};
my @mstarR = map {$_->{'logMstar(Msun/h2)'}} @{$RSPHval};
my @mhaloR = map {$_->{'logMhalo2(Msun/h)'}} @{$RSPHval};
my @rankR = map {$_->{'rank2'}} @{$RSPHval};

close $RSPHin;

while (my $row0 = $csv0->getline_hr($BSPHin)) {
	my $match_count = 0;
	my $nyuID = $row0->{nyuID};
	my $z = $row0->{zgal};
	my $mstar = $row0->{'logMstar(Msun/h2)'};
	my $mhalo = $row0->{'logMhalo2(Msun/h)'};
	my $rank = $row0->{rank2};
	foreach my $nyuIDR (@nyuIDR) {
		print ($nyuID . "," . $nyuIDR . "," . $row0 . "," . "\n");
		#if ((abs($z - $row1->{zgal}) <= 0.01) && (abs($mstar - $row1->{'logMstar(Msun/h2)'}) <= 0.3) && (abs($mhalo - $row1->{'logMhalo2(Msun/h)'}) <= 0.4) && ($rank == $row1->{rank2})) {
#			print $output0 ($nyuID . $row1->{nyuID} . "\r\n");
		#	$match_count += 1;
		#}
	}
	#print $output1 ($nyuID . "," . $match_count . "\r\n");
}
close $BSPHin;
close $output0;
close $output1;
