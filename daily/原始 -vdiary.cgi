#!/usr/local/bin/perl

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#? Web Calen v0.8 (2001/04/29)
#? Copyright(C) Kent Web 2001
#? webmaster@kent-web.com
#? http://www.kent-web.com/
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
$ver = 'Calen v0.81';
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  VDiary (2001/5/18)
#  Edit By Blue EV's Studio
#  http://evstudio.hk.st
#
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#
# [ ³]©w ]
#  public_html / index.html
#       |
#       +-- calen / calen.cgi [755]
#             |
#             +-- log [777] /
#             |
#             +-- img / book.gif pen.gif next.gif back.gif wall.gif

#============#
#  °ò¥»³]©w  #
#============#

#¼ĞÃD
$title = "VDiary";

#¼ĞÃD¦r¦â
$t_color = "#880000";

#¼ĞÃD¦r¦r«¬
$t_face = "Comic Sans MS";

# ¼ĞÃD¤j¤p
$t_size = '18pt';

# ºŞ²zªÌ±K½X
$pass = '0123';

# ¥D­¶
$home = "../index.htm";

# µ{¦¡¦W¦r.¦ì¸m
$script = "./vdiary.cgi";

# °O¿ıÀÉ¥Í¦¨¦ì¸m
$logdir = "./";

# ¹ÏÀÉ¦s©ñªº¥Ø¿ı
$imgurl = "./";

# °ò¥»¤å¦r¤j¤p
$body_size = '10pt';

# ¼ĞÃD¦rÃC¦â
$sub_color = "#0099FF";

# ¤é¾ä­I´º¦â
$tbl_color = "white";

# ¤µ¤Ñ¤é´Á­I´º¦â
$today_color = "pink";

# ¬P´Á¤»¤å¦r¦â
$sat_color = "blue";

# ¬P´Á¤é¤å¦r¦â
$sun_color = "red";

# ¯S§O¤é¤l¤å¦r¦â
$spe_color = "#F20DA2";

# ¥­¤é¤å¦r¦â
$nor_color = "black";

# ¨C¤@¹jªº¤j¤p
$width  = 35;	# ¼e
$height = 35;	# °ª

# ¥Ø¿ıÅã¥Ü³Ì·sªº¦h¤Ö½g°O¿ı
#0«h¨S¦³¥Ø¿ı
$infoview = 5;

# ¹ÏÀÉ 
$IconR = "next.gif";  #next¹Ï
$IconL = "back.gif";  #back¹Ï
$IRL_W = 80;  # ¼e
$IRL_H = 20;  # °ª

# ¦³®Ñ¼g¤é°O¦b¤é¾ä¤¤¥X²{ªº¹ÏÀÉ
$IconP = "pen.gif";
$IP_W = 18;  # ¼e
$IP_H = 19;  # °ª

# ¼ĞÃD¹Ï
$IconB = "title1.gif";

# body³]©w
$bg = $imgurl . "";	# ­I´º¹Ï
$bc = "#FFFFFF";		# ­I´º¦â
$tx = "#666666";		# ¤å¦r¦â
$lk = "#0099FF";		# ³sµ²¦â
$vl = "#0099FF";		# ¤w«ô³X³sµ²¦â
$al = "#0099FF";		# °Ê§@¤¤³sµ²¦â

# ¤@¬P´ÁÅã¥Ü¦r²´
@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

# ¯S§O¤é¤l
@SpeDay = ('0101','0211','0320','0429','0503','0504','0505',
		'0720','0915','0923','1103','1123','1223');

# °e«Hmethod (POST or GET)
$method = 'POST';

#Åã¥Ü°O¿ı®Øªº¼e«×
$tb_width = '65%';

# ¤w«ô³X³sµ²¦â
$vlink_color = "#0099ff";

# °Ê§@¤¤³sµ²¦â
$alink_color = "#666666";

# onmouseover³sµ²¦â
$hlink_color = "#0099ff";

# onmouseover³sµ²­I´º¦â
$hlink_bgcolor = "#DFEFFF";

#¤é°O³»³¡Åã¥Ü¦~¥÷ªº­I´º¦â
$calen_top = "#f0f8ff";

#¤é¾ä¥~Ãä®Ø½u¦â
$calen_bor = "#99CCFF";

#¤é¾ä¤ºÃä®Ø½u¦â
$calen_bor2 = "#99CCFF";

# ¯d¨¥¼ĞÃD«e²Å¸¹¦â
$symbol_color="#FFCC99";

# ¿é¤JÄæ/«ö¶s¤å¦r¦â
$input_color = "#666666";

# ¿é¤JÄæ/«ö¶sÃä®Ø¦â
$input_border = "#99ccff";

# ¿é¤JÄæ/«ö¶s­I´º¦â
$input_bgcolor = "#f0f8ff";

# ¿é¤JÄæ/«ö¶sonmouse over ­I´º¦â
$input_bgcolor2 = "#DFEFFF";

# ¤À¹j½uÃC¦â
$hr_color="powderblue";

#============#
#  ³]©w§¹¦¨  #
#============#

&decode;
if ($mode eq "write") { &write; }
elsif ($mode eq "admin") { &admin; }
elsif ($mode eq "check") { &check; }
&calen;

#----------------#
#  Åã¥Ü¤é¾ä  ¦  #
#----------------#
sub calen {
	local($year2) = $year;
	if ($in{'year'}) { $year = $in{'year'}; }
	if ($in{'mon'}) {
		$month = $in{'mon'};
	}
	elsif ($mode eq "view") {
		&view;
		$month = $M;
		$year  = $Y;
	}
	else {
		$month = $mon;
	}

	&header;
	print "<table border=0 cellspacing=1 cellpadding=0>\n";
	print "<tr><td><a href=\"$home\" target=\"_top\">¦^­º­¶</a></td></tr></table>\n";
	print "<center><table cellpadding=8><tr><td>\n";
	if ($IconB eq '') {
		print "<font color=\"$t_color\" size=6 face=\"$t_face\"><b><SPAN>$title</SPAN></b></font>\n";
	}
	else {
		print "<img src=\"$imgurl$IconB\"\"></td>\n";
	}
	print "</tr></table><P>\n";

#	&table("FWD", "$month");
	&table("", "$month");

	$pre = $month - 1;
	$Y1 = $year;
	if ($pre < 1) {
		$pre += 12;
		$Y1 = $year - 1;
	}
	$next = $month + 1;
	$Y2 = $year;
	if ($next > 12) {
		$next -= 12;
		$Y2 = $year + 1;
	}

	# ƒR?ƒg?[?ƒL[•\¦
	print "<a href=\"$script?mode=calen&year=$Y1&mon=$pre\"><img src=\"$imgurl$IconL\" width=\"$IRL_W\" height=\"$IRL_H\" border=0 alt=\"Back\"></a>\n";
	print "<a href=\"$script?mode=calen&year=$Y2&mon=$next\"><img src=\"$imgurl$IconR\" width=\"$IRL_W\" height=\"$IRL_H\" border=0 alt=\"Next\"></a>\n";

#	print "<table><tr><td>\n";
#	print "<form action=\"$script\" method=$method>\n";
#	print "<input type=hidden name=mode value=calen>\n";
#	print "<input type=hidden name=year value=$Y1>\n";
#	print "<input type=hidden name=mon value=$pre>\n";
#	print "<input type=submit value=' Back '></td></form>\n";
#	print "<td><form action=\"$script\" method=$method>\n";
#	print "<input type=hidden name=mode value=calen>\n";
#	print "<input type=hidden name=year value=$Y2>\n";
#	print "<input type=hidden name=mon value=$next>\n";
#	print "<input type=submit value=' Next '></td></form>\n";
#	print "</tr></table>\n";

	# ’¼ÚˆÚ“®ƒ{ƒ^?
	print "<P><table border=0><tr><td>\n";
	print "<form action=\"$script\" method=$method>\n";
	print "<select name=year class=s>\n";
	foreach ($year2-1, $year2, $year2+1) {
		if ($year == $_) {
			print "<option value=\"$_\" selected>$_ ¦~\n";
		} else {
			print "<option value=\"$_\">$_ ¦~\n";
		}
	}
	print "</select>\n<select name=mon class=s>\n";
	if ($in{'mon'} eq "") { $in{'mon'} = $mon; }
	foreach (1 .. 12) {
		if ($month == $_) {
			print "<option value=\"$_\" selected>$_ ¤ë\n";
		} else {
			print "<option value=\"$_\">$_ ¤ë\n";
		}
	}
	print "</select>\n<input type=submit value='Åã¥Ü'></td></form>\n";
	print "<td><form action=\"$script\" method=$method>\n";
	print "<input type=hidden name=mode value=allview>\n";
	print "<input type=hidden name=mon value=\"$in{'mon'}\">\n";
	$month2 = sprintf("%02d", $month);
	print "<input type=hidden name=YM value=\"$year$month2\">\n";
	print "<input type=submit value='Åã¥Ü¤µ¤ë©Ò¦³°O¨Æ'>\n";
	print "</td></form></tr></table><br><br>\n";

	# V??ƒO‚ğ’è‹`
	$newlog = $logdir . 'new.dat';

	if ($mode eq "view") {
		print "<table border=0 cellpadding=0 cellspacing=0 width='$tb_width'><tr><td width=20><img src=1.gif></td><td background=11.gif></td><td><img src=2.gif></td></tr>\n";
		print "<tr><td background=12.gif></td><td bgcolor=\"$tbl_color\">\n";
		print "<center><img src=\"$imgurl$IconP\" width=$IP_W height=$IP_H><b><font color=\"$sub_color\">$Sub</font></b>..........<b style=\"font-size:$big_size\">$Y¦~$M¤ë$D¤é ($week[$in{'w'}])</b></center>\n";
		# “ú•t‚Ì•¶?
		$body_size =~ s/(\d+)/$big_size = $1/e;
		$big_size  = ($big_size + 1) .'pt';

		print "<blockquote>$Message</bloackquote>\n";
		print "</td><td background=13.gif></td></tr><tr><td width=20><img src=3.gif></td><td background=14.gif></td><td width=20><img src=4.gif></td></tr></table>\n";

	# ?“àˆê?•\¦
	} elsif ($mode eq "allview") {
		$in{'YM'} =~ s/\D//g;
		if ($in{'YM'} =~ /^(\d\d\d\d)(\d\d)$/) {
			$Y=$1; $M=$2;
		} else {
			&error("¦~¥÷«ü©w¿ù»~!");
		}

		# ?ƒO‚ğ’è‹`
		$logfile = "$logdir$in{'YM'}\.txt";

		# ?ƒO‚Ì‘¶İ‚ğƒ`ƒFƒbƒN
		unless (-e $logfile) {
			&error("¤£¯àÅª¨ú°O¿ıÀÉ!");
		}

		open(IN,"$logfile") || &error("Open Error : $logfile");
		print "<table cellpadding=8 bgcolor=\"$tbl_color\" width=75%  border=3 cellspacing=5 bordercolor=$input_border><tr><td>\n";
		print "<center><b>$Y¦~$M¤ë©Ò¦³°O¨Æ</b></center>\n";
		print "<P><DL>\n";
		while (<IN>) {
			($Day,$Sub,$Msg) = split(/<>/);
			next if ($Sub eq "");

			print "<DT>$M/$Day - <font color=\"$sub_color\"><b>$Sub</b></font><br>\n";
			print "<DD>$Msg<P>\n";
		}
		close(IN);
		print "</DL>\n</td></tr>\n</table>\n";

	# ?Šú•\¦
	} elsif ($infoview ne "" && -e $newlog) {
		print "<table cellpadding=8 bgcolor=\"$tbl_color\" width=330  border=3 cellspacing=5 bordercolor=$input_border>\n";
		print "<tr><td><center><b>- ³Ì·s°O¿ı -</b></center><P>\n";
		open(IN,"$newlog") || &error("Open Error : $newlog");
		while (<IN>) {
			($ymd,$sub,$msg,$w) = split(/<>/);
			if ($ymd =~ /^(\d\d\d\d)(\d\d)(\d\d)/) { $md = "$2/$3"; }
			print "$md - <a href=\"$script?mode=view&YMD=$ymd&w=$w\"><b>$sub</b></a><br>\n";
		}
		close(IN);
		print "</td></tr></table>\n";
	}
	print "</center><P><div align=right>\n";
	print "<form action=\"$script\" method=$method>\n";
	print "<input type=hidden name=mode value=admin>\n";
	print "<input type=password name=pass size=8>&nbsp;";
	print "<input type=submit value='ºŞ²z'></div></form>\n";

	# µÛ§@ÅvÅã¥Ü
	print "<center><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/' target='_top'>Web Calen</a> -<br>Edit By <a href=http://evstudio.hk.st/ target=blank>Blue EV's Studio</a><!--¼s§i´¡¤J¦ì¸m--><!--#echo banner=\"\"--><!--¼s§i´¡¤J¦ì¸m-->\n";
	print "</small><br></center>\n</body>\n</html>\n";
	exit;
}
#----------------#
#  ƒJ??ƒ_•\¦  #
#----------------#
sub table {
	local($month) = $_[1];

	if ($_[0] eq "FWD") {
		$month--;
		if ($month < 1) { $month += 12; $year--; }
	}
	if ($month == $mon) { $thiskey = 1; }

	$lmon = sprintf("%02d", $month);
	open(IN,"$logdir$year$lmon\.txt");
	@lines = <IN>;
	close(IN);

	print "<TABLE BORDER=1 bordercolor=$calen_bor BGCOLOR=\"$tbl_line\" CELLSPACING=0 CELLPADDING=2>\n";
	print "<TR><TD><table border=0 cellpadding=1 cellspacing=1 bgcolor=$calen_bor2>\n";
	print "<tr><th colspan=7 bgcolor=\"$calen_top\" height=30>$year¦~ $month¤ë</th></tr><tr>\n";
	foreach (0 .. 6) {
		if ($_ == 0) { $color = $sun_color; }
		elsif ($_ == 6) { $color = $sat_color; }
		else { $color = $nor_color; }
		print "<td align=center height=20 width=$width bgcolor=\"$tbl_color\"><font color=\"$color\">$week[$_]</font></td>";
	}
	print "</tr><tr>\n";

	# •¡G‰öŠï‚È‚éuƒcƒF?[‚ÌŒö®v‚ğÀs‚µ—j“ú‚ğæ“¾ŒvZ
	$wkey = &getweek("1","$year","$month");
	$lastday = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) [$month - 1]
	+ ($month == 2 && (($year % 4 == 0 && $year % 100 != 0) ||
	$year % 400 == 0));

	$i=0; # —j“ú (ex. 0:“ú—j, 1:?—j, ... )
	$j=1; # ?—j‚Ì‘æ‰½T‚©
	$k=1; # “ú
	$flag=0;
	$spe_flag=0; # U‘Ö‹x“úƒt?ƒO
	foreach (1 .. 42) {

		# Fw’è
		if ($i == 0) { $color = $sun_color; }
		elsif ($i == 6) { $color = $sat_color; }
		else { $color = $nor_color; }

		if ($wkey eq "$i") { $flag=1; }
		if ($lastday < $k) { $flag=2; }

		if ($flag == 2 && $i == 0) { last; }

		if (!$flag) {
			print "<td align=center bgcolor=\"$tbl_color\" height=$height width=$width> - </td>";
		} elsif ($flag == 2) {
			print "<td align=center bgcolor=\"$tbl_color\" height=$height width=$width> - </td>";
		} else {
			if ($thiskey && $mday == $k) {
				print "<td align=center valign=top bgcolor=\"$today_color\" height=$height width=$width>";
			} else {
				print "<td align=center valign=top bgcolor=\"$tbl_color\" height=$height width=$width>";
			}

			$lday = sprintf("%02d", $k);
			$this = $lmon . $lday;

			# U‘Ö‹x“ú
			if ($spe_flag) {
				$spe_flag=0;
				$color = $spe_color;
			} else {
				# j“ú‚P
				foreach $x (@SpeDay) {
					if ($x eq "$this") {
						if ($i == 0) { $spe_flag=1; }
						$color = $spe_color;
						last;
					}
				}
				# j“ú‚Q
				while (($N, $V) = each(%SpeDay)) {
					if ($month == $N && $i == 1 && $j == $V) {
						$color = $spe_color;
						last;
					}
				}
			}

			print "<a href=\"$script?mode=write&YMD=$year$lmon$lday&w=$i\">";
			print "<font color=\"$color\">$k</font></a><br>\n";
			local($Day,$Sub,$Comment) = split(/<>/, $lines[$k-1]);
			if ($Sub ne "") {
				print "<a href=\"$script?mode=view&YMD=$year$lmon$lday&w=$i\"><img src=\"$imgurl$IconP\" border=0 width=$IP_W height=$IP_H></a>";
#				if ($infoview > 0) {
#				unshift(@TOP,"$lines[$k-1]$year$lmon$lday<>$i<>");
#				$infoview--;
#				}
			}
			else { $DAY = $k; }

			print "</td>";
		}
		if ($flag && $i == 1) { $j++; }
		$i++;
		if ($flag) { $k++; }
		if ($i == 7) { print "</tr><tr>\n"; $i=0; }
	}
	print "</tr></table></TD></TR></TABLE><br>\n";
}

#--------------------#
#  “ú‹L?ƒO“Ç‚İo‚µ  #
#--------------------#
sub view {
	if ($in{'YMD'} =~ /^(\d\d\d\d)(\d\d)(\d\d)$/) {
		$Y=$1; $M=$2; $D=$3;
	} else {
		&error("¤é´Á¿ù»~¿é¤J");
	}
	$logfile = "$logdir$Y$M\.txt";

	open(IN,"$logfile") || &error("Open Error : $logfile");
	while (<IN>) {
		($Day,$Sub,$Message) = split(/<>/);
		if ($Day == $D) { last; }
	}
	close(IN);

	return ($Day,$Sub,$Message,$Y);
}

#--------------#
#  ??‚İ‰æ–Ê  #
#--------------#
sub write {
	if ($in{'YMD'} =~ /^(\d\d\d\d)(\d\d)(\d\d)$/) {
		$Y=$1; $M=$2; $D=$3;
	} else {
		&error("¤é´Á¿ù»~¿é¤J!");
	}

	# ƒpƒX?[ƒhƒ`ƒFƒbƒN
	if ($in{'pass'} eq "") {

		$flag=0;
		open(IN,"$logdir$Y$M\.txt");
		while (<IN>) {
			local($day,$sub,$msg) = split(/<>/);
			if ($D == $day && $sub ne "") { $flag=1; last; }
		}
		close(IN);

		&header;
		print "<br><br><center>°Ê§@¹ï¶H¤é´Á <b>$Y¤é$M¤ë$D¤é</b><br>\n";
		print "<P><b>- ½Ğ¿é¤J±K½X-</b>\n";
		print "<form action=\"$script\" method=$method>\n";
		print "<input type=hidden name=mode value=write>\n";
		print "&nbsp;<input type=hidden name=YMD value=\"$in{'YMD'}\">\n";
		print "&nbsp;<input type=hidden name=w value=\"$in{'w'}\">\n";

		if ($flag) {
			print "<select name=action class=s>\n";
			print "<option value=\"edit\">­×§ï\n";
			print "<option value=\"del\">§R°£\n";
			print "</select>\n";
		}
		print "<input type=password name=pass size=8>";
		print "&nbsp;<input type=submit value=' ½T©w '></form>\n";
	print "<center><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/' target='_top'>Web Calen</a> -<br>Edit By <a href=http://evstufio.hk.st/ target=blank>Blue EV's Studio</a><!--¼s§i´¡¤J¦ì¸m--><!--#echo banner=\"\"--><!--¼s§i´¡¤J¦ì¸m-->\n";
	print "</small><br></center>\n</body>\n";
		exit;
	}
	elsif ($in{'pass'} ne "$pass") { &error("±K½X¿ù»~!!"); }

	# ?‚«?‚İ??
	if ($in{'action'} eq "regist") {
		$flag=0;

		if ($in{'sub'} eq "") { &error("¨S¦³¿é¤J¼ĞÃD"); }
		if ($in{'message'} eq "") { &error("¨S¦³¿é¤J¤é°O¤º®e"); }
		if ($in{'wrap'} ne "on") { $in{'message'} =~ s/<br>//ig; }

		# ?ƒOƒtƒ@ƒC?‚ğ’è‹`
		$logfile = "$logdir$Y$M\.txt";

		# ?ƒO‚ª‘¶İ‚·‚é‚Æ‚«
		if (-e $logfile) {
			@new=();
			open(IN,"$logfile") || &error("Open Error : $logfile");
			while (<IN>) {
				($Day,$Sub,$Msg) = split(/<>/);
				if ($D eq "$Day") {
					$_="$Day<>$in{'sub'}<>$in{'message'}<>\n";
				}
				push(@new,$_);
			}
			close(IN);
		}
		# ?ƒO‚ª‘¶İ‚µ‚È‚¢‚Æ‚«
		else {
			$flag=1;
			@new=();
			foreach (1 .. 31) {
				$_ = sprintf("%02d", $_);
				if ($D eq "$_") {
					$log = "$_<>$in{'sub'}<>$in{'message'}<>\n";
				} else {
					$log = "$_<><><>\n";
				}
				push(@new,$log);
			}
		}

		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);

		# V‹K?ƒO‚Ìƒp[ƒ~ƒbƒV??‚ğ666‚Ö
		if ($flag) { chmod(0666,$logfile); }

		# V??ƒOXV??
		if ($infoview > 0) {
			$newlog = $logdir . 'new.dat';
			unless (-e $newlog) {
				$new_flag=1;
				$new2[0] = "$in{'YMD'}<>$in{'sub'}<>$in{'message'}<>$in{'w'}<>\n";
			} else {
				open(IN,"$newlog") || &error("Open Error : $newlog");
				@lines = <IN>;
				close(IN);
				while ($infoview <= @lines) { pop(@lines); }

				@new2=();
				$flag2=0;
				foreach (@lines) {
					($ymd,$sub,$msg,$w) = split(/<>/);
					if ($in{'YMD'} == $ymd) {
						$flag2=1;
						$_ = "$ymd<>$in{'sub'}<>$in{'message'}<>$w<>\n";
					} elsif (!$flag2 && $in{'YMD'} > $ymd) {
						$flag2=1;
						push(@new2,"$in{'YMD'}<>$in{'sub'}<>$in{'message'}<>$in{'w'}<>\n");
					}
					push(@new2,$_);
				}
				if (!$flag2) {
					push(@new2,"$in{'YMD'}<>$in{'sub'}<>$in{'message'}<>$in{'w'}<>\n");
				}
			}
			# XV
			open(OUT,">$newlog") || &error("Write Error : $newlog");
			print OUT @new2;
			close(OUT);

			# V‹K?ƒO‚Ìƒp[ƒ~ƒbƒV??‚ğ666‚Ö
			if ($new_flag) { chmod(0666,$newlog); }
		}

		# Š®—¹?ƒbƒZ[ƒW
		&header;
		print "<center><h3>¥H¤U°O¿ı¤w¸g¥¿±`°e¥X</h3>\n";
		print "<table cellpadding=8 bgcolor=\"$tbl_color\" width=65%  border=3 cellspacing=5 bordercolor=$input_border><tr><td>\n";
		print "¤é´ÁF <b>$Y¦~$M¤ë$D¤é</b><br>\n";
		print "¼ĞÃDF <b>$in{'sub'}</b><br><br>\n";
		print "$in{'message'}\n</td></tr></table>\n";
		print "<P><form action=\"$script\" method=\"$method\">\n";
		print "<input type=submit value='¦^¨ì¥Dµe­±'></form>\n";
	print "<center><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/' target='_top'>Web Calen</a> -<br>Edit By <a href=http://evstufio.hk.st/ target=blank>Blue EV's Studio</a><!--¼s§i´¡¤J¦ì¸m--><!--#echo banner=\"\"--><!--¼s§i´¡¤J¦ì¸m-->\n";
	print "</small><br></center>\n</body>\n";
		exit;
	}
	# ?ƒOí?
	elsif ($in{'action'} eq "del") {
		$logfile = "$logdir$Y$M\.txt";
		@new=();
		open(IN,"$logfile") || &error("Open Error : $logfile");
		while (<IN>) {
			($day,$sub,$msg) = split(/<>/);
			if ($D eq "$day") {
				$_="$day<><><>\n";
			}
			push(@new,$_);
		}
		close(IN);

		open(OUT,">$logfile") || &error("Write Error : $logfile");
		print OUT @new;
		close(OUT);

		# V??ƒO
		if ($infoview > 0) {
			$newlog = $logdir . 'new.dat';
			open(IN,"$newlog") || &error("Open Error : $newlog");
			$flag=0;
			@new=();
			while (<IN>) {
				($ymd,$sub,$msg) = split(/<>/);
				if ($in{'YMD'} == $ymd) { $flag=1; next; }
				push(@new,$_);
			}
			close(IN);

			# ŠY??ƒO‚Ì?‚éê?‚ÍV??ƒOXV
			if ($flag) {
				open(OUT,">$newlog") || &error("Write Error : $newlog");
				print OUT @new;
				close(OUT);
			}
		}

		# Š®—¹?ƒbƒZ[ƒW
		&header;
		print "<center><h3>§R°£§¹¦¨</h3>\n";
		print "<form action=\"$script\" method=\"$method\">\n";
		print "<input type=submit value='¦^¨ì¥Dµe­±'></form>\n";
		print "</center>\n</body>\n</html>\n";
		exit;
	}
	# ?ƒOC³‚Ìê?
	elsif ($in{'action'} eq "edit") {
		local($flag)=0;
		open(IN,"$logdir$Y$M\.txt") || &error("Open Error : $logdir$Y$M\.txt");
		while (<IN>) {
			($day,$sub,$msg) = split(/<>/);
			if ($day eq "$D") { $flag=1; last; }
		}
		close(IN);
		if (!$flag) { &error("§ä¤£¨ì¸Ó½g¯d¨¥"); }
		$msg =~ s/<br>/\r/g;
	}

	&header;
	print <<"EOM";
<center>
<h3>¤é°O®Ñ¼g</h3>
<table><tr><td>
<LI>¥i¥H¨Ï¥Îhtml»yªk
<LI>¦p¿ï¾Ü§ï¦æ¦³®Ä§Y¥i«öenter§ï¦æ.§_«h¬°±j¦æ§ï¦æ
</td></tr></table>
<form action="$script" method="$method">
<input type=hidden name=mode value="write">
<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=action value="regist">
<input type=hidden name=YMD value="$in{'YMD'}">
<input type=hidden name=w value="$in{'w'}">
<table border=1 cellpadding=5 cellspacing=0>
<tr>
  <td>¤é´Á</td><td><b>$Y¦~$M¤ë$D¤é</b></td>
</tr>
<tr>
  <td>¼ĞÃD</td><td><input type=text name=sub size=30 value="$sub"></td>
</tr>
<tr>
  <td colspan=2>
    §ï¦æ¤è¦¡&nbsp;&nbsp;&nbsp;
    <input type=checkbox name=wrap value=on checked>§ï¦æ¦³®Ä<br>
    <textarea name=message cols=44 rows=6 wrap=soft>$msg</textarea><br>
    <input type=submit value="½T©w">&nbsp;<input type=reset value="²M°£">
  </td>
</tr>
</table>
</form>
</center>
</body>
</html>
EOM
	exit;
}

#--------------#
#  ŠÇ?Ò‰æ–Ê  #
#--------------#
sub admin {
	if ($in{'pass'} ne "$pass") { &error("ºŞ²zªÌ±K½X¿ù»~!"); }

	if ($DEL[0]) {
		if ($infoview > 0) {
			$newlog = $logdir . 'new.dat';
			open(IN,"$newlog") || &error("Open Error : $newlog");
			@lines = <IN>;
			close(IN);
		}

		&header;
		print "<center>\n";
		foreach (@DEL) {
			if (unlink ("$logdir$_")) {
				print "§R°£§¹²¦ !<b>$_</b><br>\n";
			} else {
				print "§R°£¥¢±Ñ !<b>$_</b><br>\n";
			}

			# V??ƒOƒ`ƒFƒbƒN
			if ($infoview > 0) {
				$flag=0;
				$_ =~ s/^(\d+)/$key1 = $1/e;
				foreach (@lines) {
					($ymd,$sub,$msg) = split(/<>/);
					$ymd =~ s/^(\d\d\d\d\d\d)(\d\d)/$key2 = $1/e;
					if ($key1 == $key2) { $flag=1; next; }
					push(@new,$_);
				}
			}
		}
		# ŠY??ƒO‚Ì?‚éê?‚ÍV??ƒOXV
		if ($flag) {
			open(OUT,">$newlog") || &error("Write Error : $newlog");
			print OUT @new;
			close(OUT);
		}

		print "<form action=\"$script\" method=\"$method\">\n";
		print "<input type=submit value='¦^¨ì¥Dµe­±'></form>\n";
		print "</center>\n</body>\n</html>\n";
		exit;
	} else {
		opendir(DIR,"$logdir") || &error("Open Error : $logdir");
		@data = readdir(DIR);
		closedir(DIR);
	}

	&header;
	print <<"EOM";
<center>
<h2>ºŞ²z°Ï°ì</h2>
- ¿ï¾Ü±ı§R°£ªº°O¨Æ¦A«öÁä½T©w«K¥i§R°£<b>¸Ó¤ë</b>©Ò¦³°O¿ı -
<form action="$script" method="$method">
<input type=hidden name=mode value="admin">
<input type=hidden name=pass value="$in{'pass'}">
<input type=submit value="§R°£">  <input type=reset value="²M°£">
<P><table border=2 cellspacing=5 bordercolor=$input_border width=55%>
<tr><th>§R°£</th><th>¤é´Á</th><th>®e¶q</th></tr>
EOM
	$all=0;
	$size=0;
	foreach (@data) {
		if ($_ =~ /(\d\d\d\d)(\d\d)\.txt/) {

			# ƒtƒ@ƒC?ƒTƒCƒY
			$size = -s "$logdir$_";

			print "<tr><th><input type=checkbox name=del value=\"$_\"></th>";
			print "<td>$1¦~$2¤ë</td><td>$size Bytes</td></tr>\n";

			$all += $size;
		}
	}
	print "</table></form>\n";
	print "<P>Á`®e¶q: <b>$all</b> Bytes\n";
	print "</center>\n</body>\n</html>\n";
	exit;
}

#----------------#
#  ƒfƒR[ƒh??  #
#----------------#
sub decode {
	local($name,$value,@pairs);

	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }
	@pairs = split(/&/, $buffer);
	foreach (@pairs) {
		($name, $value) = split(/=/);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

		# ‹Ö~‹L?
		$value =~ s/<>/&lt;&gt;/g;

		# ‰üs??
		if ($name eq "message") {
			$value =~ s/\r\n/<br>/g;
			$value =~ s/\n/<br>/g;
			$value =~ s/\r/<br>/g;
		} else {
			$value =~ s/\r//g;
			$value =~ s/\n//g;
		}

		# í?î•ñ
		if ($name eq 'del') { push(@DEL,$value); }

		$in{$name} = $value;
	}
	$mode = $in{'mode'};
	$in{'YMD'} =~ s/\D//g;

	# “ú?‚Ìæ“¾
	$ENV{'TZ'} = "JST-8";
	($sec,$min,$hour,$mday,$mon,$year,$wday,$dmy) = localtime(time);
	$year += 1900;
	$mon++;

	# “ú?‚ÌƒtƒH[ƒ}ƒbƒg
	$DATE = sprintf("%04d/%02d/%02d(%s) %02d:%02d",
			$year,$mon,$mday,$week[$wday],$hour,$min);
}

#--------------#
#  HTMLƒwƒbƒ_  #
#--------------#
sub header {
	$head_flag=1;
	print <<"EOM";
Content-type: text/html

<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=big5">
<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
<STYLE TYPE="text/css">
<!--
body,tr,td,th { font-size:$body_size }
small { font-size:9pt }
A { text-decoration: none; }
a:visited	{color : $vlink_color; text-decoration : none; }
a:active	{color : $alink_color; text-decoration : none; }
a:hover	{color : $hlink_color; text-decoration : underline overline blink; background-color : $hlink_bgcolor;
}
input,textarea{border-left:1px solid $input_border; font-family:Comic Sans MS,·s²Ó©úÅé;
border-right:2px solid $input_border;
border-top:1px solid $input_border;
border-bottom:2px solid $input_border;
background-color : $input_bgcolor; color : $input_color; }
.s{border-left:1px solid $input_border; font-family:·s²Ó©úÅé;
border-right:2px solid $input_border;
border-top:1px solid $input_border;
border-bottom:2px solid $input_border;
background-color : $input_bgcolor; color : $input_color; }
-->
</STYLE>
<title>$title</title></head>
<body background="$bg" bgcolor="$bc" text="$tx" link="$lk" vlink="$vl" alink="$al">
EOM
}

#--------------#
#  ƒG?[??  #
#--------------#
sub error {
	&header if (!$head_flag);
	print "<center><h3>ERROR !</h3>\n";
	print "<P><font color=red>$_[0]</font>\n";
	print "</center>\n</body>\n</html>\n";
	exit;
}

#-------------------------------#
#  ƒcƒF?[‚ÌŒö®i—j“ú‚Ìæ“¾j #
#-------------------------------#
sub getweek {
	local($day, $year, $month) = @_;
	# $year  = ”N; # 4?
	# $month = ?; # 1-12 --> 1?‚Í1

	if ($month == 1 || $month == 2) {
		$year--;
		$month += 12;
	}

	int ($year + int ($year/4) - int ($year/100) + int ($year/400) + int ((13*$month+8)/5) + $day) % 7;
}

#------------------#
#  ƒ`ƒFƒbƒN?[ƒh  #
#------------------#
sub check {
	&header;
	print "<h2>Check Mode</h2>\n<UL>\n";

	if (-d $logdir) { print "<LI>°O¿ıÀÉÅª¨ú!FOK\n"; }
	else { print "<LI>°O¿ıÀÉÅª¨ú!FNG ¨ $logdir\n"; }

	if (-r $logdir && -w $logdir && -x $logdir) {
		print "<LI>°O¿ıÀÉÅª¨úFOK\n";
	} else {
		print "<LI>°O¿ıÀÉÅª¨úFNG ¨ $logdir\n";
	}

	print "</UL>\n</body>\n</html>\n";
	exit;
}
