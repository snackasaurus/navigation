#!/usr/bin/perl
#
# Eric Jiang
# http://notes.ericjiang.com/posts/54
# This software is public domain.
#
use bytes;

my $data;

#prevents us from repeating messages
my $waitingflag = 0;

while (1) {

    $data = `sudo cat /dev/hidraw2 | head -c 7`;

    my $report = ord(substr($data, 0, 1));
    my $status = ord(substr($data, 1, 1));
    my $unit   = ord(substr($data, 2, 1));
    my $exp    = ord(substr($data, 3, 1));
    my $lsb    = ord(substr($data, 4, 1));
    my $msb    = ord(substr($data, 5, 1));
    my $weight = ($msb * 256 + $lsb) / 10;
    if($exp != 255 && $exp != 0) {
        $weight ^= $exp;
    }
    #print "$report $status $unit $exp $weight\n";

    if($report != 0x03) {
      die "Error reading scale data!\n";
    }

    if ($status == 0x04) {
        my $unitName = "units";
        if($unit == 11) {
            $unitName = "ounces";
        } elsif ($unit == 12) {
            $unitName = "pounds";
        }
	my $filename = 'data.txt';
	open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";
	print $fh "$weight";
        print "$weight $unitName\n";
        last;
    } else {
        die "Unknown status code: $status\n";
    }
}
