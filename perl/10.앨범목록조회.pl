#!/usr/bin/perl

use strict;
use warnings;

use lib "lib";
use Https;
use Prop;
use Json;

my $prop = Prop->new("info.txt", " ");
my ($access_token, $band_key) = $prop->gets("access_token", "band_key");

printf "access_token: %s\n", $access_token;
printf "band_key: %s\n", $band_key;

my $https = Https->new;
$https->host("openapi.band.us")
    ->url("/v2/band/albums")
    ->param("access_token", $access_token)
    ->param("band_key", $band_key)
    ;
my $result = $https->get();
my $json = Json->new;
$json->load_text($result);
print $json->pretty_json;
print "\n";
