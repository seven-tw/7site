#!/usr/local/bin/perl

$title = "||||||| Digital Diary |||||||";

$t_color = "#CCCCCC";

$t_face = "Arial, Helvetica, sans-serif";

$t_size = '9pt';

$pass = 'king3137';

$home = "../index.htm";

$script = "./diary.cgi";

$logdir = "./";

$imgurl = "./";

$body_size = '9pt';

$sub_color = "#FF9900";

$tbl_color = "white";

$today_color = "#F0F5FD";

$sat_color = "#6666FF";

$sun_color = "#CC3366";

$spe_color = "#FF00CC";

$nor_color = "#999999";

$width  = 35;
$height = 35;

$infoview = 1;

$IconR = "next.gif";
$IconL = "back.gif";
$IRL_W = 57;
$IRL_H = 19;

$IconP = "7up.gif";
$IP_W = 27;
$IP_H = 22;

$IconB = "ddtitle.gif";

$bg = $imgurl . "";
$bc = "#99CCFF";
$tx = "#666666";
$lk = "#0099FF";
$vl = "#0099FF";
$al = "#0099FF";

@week = ('SUN','MON','TUE','WED','THU','FRI','SAT');

@SpeDay = ('0101','0214','0922','1225','1231');

$method = 'POST';

$tb_width = '90%';

$vlink_color = "#0099ff";

$alink_color = "#3333FF";

$hlink_color = "#0099ff";

$hlink_bgcolor = "";

$calen_top = "#F0F5FD";

$calen_bor = "#99CCFF";

$calen_bor2 = "#99CCFF";

$symbol_color="#FFCC99";

$input_color = "#666666";

$input_border = "#999999";

$input_bgcolor = "#ECF5FD";

$input_bgcolor2 = "#DFEFFF";

$hr_color="powderblue";


&decode;
if ($mode eq "write") { &write; }
elsif ($mode eq "admin") { &admin; }
elsif ($mode eq "check") { &check; }
&calen;


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
	print "<center><table cellpadding=0><tr><td>\n";
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

	# ÉR?Ég?Å[?ÉLÅ[ï\é¶
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

	# íºê⁄à⁄ìÆÉ{É^?
	print "<P><table border=0><tr><td>\n";
	print "<form action=\"$script\" method=$method>\n";
	print "<select name=year class=s>\n";
	foreach ($year2-1, $year2, $year2+1) {
		if ($year == $_) {
			print "<option value=\"$_\" selected>$_ ¶~\n";
		} else {
			print "<option value=\"$_\">$_ ¶~\n";
		}
	}
	print "</select>\n<select name=mon class=s>\n";
	if ($in{'mon'} eq "") { $in{'mon'} = $mon; }
	foreach (1 .. 12) {
		if ($month == $_) {
			print "<option value=\"$_\" selected>$_ §Î\n";
		} else {
			print "<option value=\"$_\">$_ §Î\n";
		}
	}
	print "</select>\n<input type=submit value='≈„•‹'></td></form>\n";
	print "<td><form action=\"$script\" method=$method>\n";
	print "<input type=hidden name=mode value=allview>\n";
	print "<input type=hidden name=mon value=\"$in{'mon'}\">\n";
	$month2 = sprintf("%02d", $month);
	print "<input type=hidden name=YM value=\"$year$month2\">\n";
	print "<input type=submit value='≈„•‹§µ§Î©“¶≥∞O®∆'>\n";
	print "</td></form></tr></table><br><br>\n";

	# êV??ÉOÇíËã`
	$newlog = $logdir . 'new.dat';

	if ($mode eq "view") {
		print "<table border=0 cellpadding=0 cellspacing=2 width='$tb_width' bgcolor=\"$tbl_color\"><tr></tr>\n";
		print "<tr><td bgcolor=\"$tbl_color\">\n";
		print "<center><b><font color=\"$sub_color\">$Sub</font></b> / <b style=\"font-size:$big_size\">$Y¶~$M§Î$D§È ($week[$in{'w'}])</b></center>\n";
		$body_size =~ s/(\d+)/$big_size = $1/e;
		$big_size  = ($big_size + 1) .'pt';

		print "<blockquote>$Message</bloackquote>\n";
		print "</td></table>\n";

	# ?ì‡àÍ?ï\é¶
	} elsif ($mode eq "allview") {
		$in{'YM'} =~ s/\D//g;
		if ($in{'YM'} =~ /^(\d\d\d\d)(\d\d)$/) {
			$Y=$1; $M=$2;
		} else {
			&error("¶~•˜´¸©wø˘ª~!");
		}

		# ?ÉOÇíËã`
		$logfile = "$logdir$in{'YM'}\.txt";

		# ?ÉOÇÃë∂ç›ÇÉ`ÉFÉbÉN
		unless (-e $logfile) {
			&error("§£Ø‡≈™®˙∞Oø˝¿…!");
		}

		open(IN,"$logfile") || &error("Open Error : $logfile");
		print "<table cellpadding=0 bgcolor=\"$tbl_color\" width=90%  border=0 cellspacing=5 bordercolor=$input_border><tr><td>\n";
		print "<center><b>$Y¶~$M§Î©“¶≥∞O®∆</b></center>\n";
		print "<P><DL>\n";
		while (<IN>) {
			($Day,$Sub,$Msg) = split(/<>/);
			next if ($Sub eq "");

			print "<DT>$M/$Day - <font color=\"$sub_color\"><b>$Sub</b></font><br>\n";
			print "<DD>$Msg<P>\n";
		}
		close(IN);
		print "</DL>\n</td></tr>\n</table>\n";

	# ?ä˙ï\é¶
	} elsif ($infoview ne "" && -e $newlog) {
		print "<table cellpadding=0 bgcolor=\"$tbl_color\" width=330  border=0 cellspacing=5 bordercolor=$input_border>\n";
		print "<tr><td><center><b>- ≥Ã∑s∞Oø˝ -</b></center><P>\n";
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
	print "<input type=submit value='§C∏π±M•Œ'></div></form>\n";

	print "<center><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/' target=blank>Web Calen</a> edit by <a href=http://evstudio.hk.st/ target=blank>Blue EV's Studio</a> -<br>Visual Design by Seven\n";
	print "</small><br></center>\n</body>\n</html>\n";
	exit;
}

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
	print "<TR><TD><table border=0 cellpadding=1 cellspacing=0 bgcolor=$calen_bor2>\n";
	print "<tr><th colspan=7 bgcolor=\"$calen_top\" height=30>$year¶~ $month§Î</th></tr><tr>\n";
	foreach (0 .. 6) {
		if ($_ == 0) { $color = $sun_color; }
		elsif ($_ == 6) { $color = $sat_color; }
		else { $color = $nor_color; }
		print "<td align=center height=20 width=$width bgcolor=\"$tbl_color\"><font color=\"$color\">$week[$_]</font></td>";
	}
	print "</tr><tr>\n";

	# ï°éGâˆäÔÇ»ÇÈÅuÉcÉF?Å[ÇÃåˆéÆÅvÇé¿çsÇµójì˙ÇéÊìæåvéZ
	$wkey = &getweek("1","$year","$month");
	$lastday = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31) [$month - 1]
	+ ($month == 2 && (($year % 4 == 0 && $year % 100 != 0) ||
	$year % 400 == 0));

	$i=0; # ójì˙ (ex. 0:ì˙ój, 1:?ój, ... )
	$j=1; # ?ójÇÃëÊâΩèTÇ©
	$k=1; # ì˙
	$flag=0;
	$spe_flag=0; # êUë÷ãxì˙Ét?ÉO
	foreach (1 .. 42) {

		# êFéwíË
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

			# êUë÷ãxì˙
			if ($spe_flag) {
				$spe_flag=0;
				$color = $spe_color;
			} else {
				# èjì˙ÇP
				foreach $x (@SpeDay) {
					if ($x eq "$this") {
						if ($i == 0) { $spe_flag=1; }
						$color = $spe_color;
						last;
					}
				}
				# èjì˙ÇQ
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


sub view {
	if ($in{'YMD'} =~ /^(\d\d\d\d)(\d\d)(\d\d)$/) {
		$Y=$1; $M=$2; $D=$3;
	} else {
		&error("§È¥¡ø˘ª~øÈ§J");
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


sub write {
	if ($in{'YMD'} =~ /^(\d\d\d\d)(\d\d)(\d\d)$/) {
		$Y=$1; $M=$2; $D=$3;
	} else {
		&error("§È¥¡ø˘ª~øÈ§J!");
	}

	# ÉpÉX?Å[ÉhÉ`ÉFÉbÉN
	if ($in{'pass'} eq "") {

		$flag=0;
		open(IN,"$logdir$Y$M\.txt");
		while (<IN>) {
			local($day,$sub,$msg) = split(/<>/);
			if ($D == $day && $sub ne "") { $flag=1; last; }
		}
		close(IN);

		&header;
		print "<br><br><center>µn§J§È¥¡<b>$Y§È$M§Î$D§È</b><br>\n";
		print "<P><b>- §C∏π±M•Œ°E§J•ﬂ∏T§Ó -</b>\n";
		print "<form action=\"$script\" method=$method>\n";
		print "<input type=hidden name=mode value=write>\n";
		print "&nbsp;<input type=hidden name=YMD value=\"$in{'YMD'}\">\n";
		print "&nbsp;<input type=hidden name=w value=\"$in{'w'}\">\n";

		if ($flag) {
			print "<select name=action class=s>\n";
			print "<option value=\"edit\">≠◊ßÔ\n";
			print "<option value=\"del\">ßR∞£\n";
			print "</select>\n";
		}
		print "<input type=password name=pass size=8>";
		print "&nbsp;<input type=submit value=' µn§J '></form>\n";
	print "<center><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/' target=blank>Web Calen</a> edit by <a href=http://evstudio.hk.st/ target=blank>Blue EV's Studio</a> -<br>Visual Design by Seven\n";
	print "</small><br></center>\n</body>\n";
		exit;
	}
	elsif ($in{'pass'} ne "$pass") { &error("µn§J±KΩXø˘ª~!!"); }

	# ?Ç´?Ç›??
	if ($in{'action'} eq "regist") {
		$flag=0;

		if ($in{'sub'} eq "") { &error("®S¶≥øÈ§Jº–√D"); }
		if ($in{'message'} eq "") { &error("®S¶≥øÈ§J§È∞O§∫Æe"); }
		if ($in{'wrap'} ne "on") { $in{'message'} =~ s/<br>//ig; }

		# ?ÉOÉtÉ@ÉC?ÇíËã`
		$logfile = "$logdir$Y$M\.txt";

		# ?ÉOÇ™ë∂ç›Ç∑ÇÈÇ∆Ç´
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
		# ?ÉOÇ™ë∂ç›ÇµÇ»Ç¢Ç∆Ç´
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

		# êVãK?ÉOÇÃÉpÅ[É~ÉbÉV??Ç666Ç÷
		if ($flag) { chmod(0666,$logfile); }

		# êV??ÉOçXêV??
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
			# çXêV
			open(OUT,">$newlog") || &error("Write Error : $newlog");
			print OUT @new2;
			close(OUT);

			# êVãK?ÉOÇÃÉpÅ[É~ÉbÉV??Ç666Ç÷
			if ($new_flag) { chmod(0666,$newlog); }
		}

		# äÆóπ?ÉbÉZÅ[ÉW
		&header;
		print "<center><h3>•H§U∞Oø˝•ø±`∞e•X</h3>\n";
		print "<table cellpadding=0 bgcolor=\"$tbl_color\" width=80%  border=0 cellspacing=5 bordercolor=$input_border><tr><td>\n";
		print "§È¥¡ÅF <b>$Y¶~$M§Î$D§È</b><br>\n";
		print "º–√DÅF <b>$in{'sub'}</b><br><br>\n";
		print "$in{'message'}\n</td></tr></table>\n";
		print "<P><form action=\"$script\" method=\"$method\">\n";
		print "<input type=submit value='¶^®Ï•Dµe≠±'></form>\n";
	print "<center><small><!-- $ver -->\n";
	print "- <a href='http://www.kent-web.com/' target=blank>Web Calen</a> edit by <a href=http://evstudio.hk.st/ target=blank>Blue EV's Studio</a> -<br>Visual Design by Seven\n";
	print "</small><br></center>\n</body>\n";
		exit;
	}
	# ?ÉOçÌ?
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

		# êV??ÉO
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

			# äY??ÉOÇÃ?ÇÈèÍ?ÇÕêV??ÉOçXêV
			if ($flag) {
				open(OUT,">$newlog") || &error("Write Error : $newlog");
				print OUT @new;
				close(OUT);
			}
		}

		# äÆóπ?ÉbÉZÅ[ÉW
		&header;
		print "<center><h3>ßR∞£ßπ¶®</h3>\n";
		print "<form action=\"$script\" method=\"$method\">\n";
		print "<input type=submit value='¶^®Ï•Dµe≠±'></form>\n";
		print "</center>\n</body>\n</html>\n";
		exit;
	}
	# ?ÉOèCê≥ÇÃèÍ?
	elsif ($in{'action'} eq "edit") {
		local($flag)=0;
		open(IN,"$logdir$Y$M\.txt") || &error("Open Error : $logdir$Y$M\.txt");
		while (<IN>) {
			($day,$sub,$msg) = split(/<>/);
			if ($day eq "$D") { $flag=1; last; }
		}
		close(IN);
		if (!$flag) { &error("ß‰§£®Ï∏”ΩgØd®•"); }
		$msg =~ s/<br>/\r/g;
	}

	&header;
	print <<"EOM";
<center>
<h3>§È∞OÆ—ºg</h3>
<table><tr><td>
<LI>•i•H®œ•Œhtmlªy™k
<LI>¶pøÔæ‹ßÔ¶Ê¶≥ÆƒßY•i´ˆenterßÔ¶Ê.ß_´h¨∞±j¶ÊßÔ¶Ê
</td></tr></table>
<form action="$script" method="$method">
<input type=hidden name=mode value="write">
<input type=hidden name=pass value="$in{'pass'}">
<input type=hidden name=action value="regist">
<input type=hidden name=YMD value="$in{'YMD'}">
<input type=hidden name=w value="$in{'w'}">
<table border=0 cellpadding=5 cellspacing=0>
<tr>
  <td>§È¥¡</td><td><b>$Y¶~$M§Î$D§È</b></td>
</tr>
<tr>
  <td>º–√D</td><td><input type=text name=sub size=30 value="$sub"></td>
</tr>
<tr>
  <td colspan=2>
    ßÔ¶Ê§Ë¶°&nbsp;&nbsp;&nbsp;
    <input type=checkbox name=wrap value=on checked>ßÔ¶Ê¶≥Æƒ<br>
    <textarea name=message cols=44 rows=6 wrap=soft>$msg</textarea><br>
    <input type=submit value="ΩT©w">&nbsp;<input type=reset value="≤M∞£">
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


sub admin {
	if ($in{'pass'} ne "$pass") { &error("µn§J±KΩXø˘ª~!"); }

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
				print "ßR∞£ßπ≤¶ !<b>$_</b><br>\n";
			} else {
				print "ßR∞£•¢±— !<b>$_</b><br>\n";
			}

			# êV??ÉOÉ`ÉFÉbÉN
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
		# äY??ÉOÇÃ?ÇÈèÍ?ÇÕêV??ÉOçXêV
		if ($flag) {
			open(OUT,">$newlog") || &error("Write Error : $newlog");
			print OUT @new;
			close(OUT);
		}

		print "<form action=\"$script\" method=\"$method\">\n";
		print "<input type=submit value='¶^®Ï•Dµe≠±'></form>\n";
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
<h2>∫ﬁ≤z∞œ∞Ï</h2>
- øÔæ‹±˝ßR∞£™∫∞O®∆¶A´ˆ¡‰ΩT©w´K•ißR∞£<b>∏”§Î</b>©“¶≥∞Oø˝ -
<form action="$script" method="$method">
<input type=hidden name=mode value="admin">
<input type=hidden name=pass value="$in{'pass'}">
<input type=submit value="ßR∞£">  <input type=reset value="≤M∞£">
<P><table border=2 cellspacing=5 bordercolor=$input_border width=55%>
<tr><th>ßR∞£</th><th>§È¥¡</th><th>Æe∂q</th></tr>
EOM
	$all=0;
	$size=0;
	foreach (@data) {
		if ($_ =~ /(\d\d\d\d)(\d\d)\.txt/) {

			# ÉtÉ@ÉC?ÉTÉCÉY
			$size = -s "$logdir$_";

			print "<tr><th><input type=checkbox name=del value=\"$_\"></th>";
			print "<td>$1¶~$2§Î</td><td>$size Bytes</td></tr>\n";

			$all += $size;
		}
	}
	print "</table></form>\n";
	print "<P>¡`Æe∂q: <b>$all</b> Bytes\n";
	print "</center>\n</body>\n</html>\n";
	exit;
}


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

		# ã÷é~ãL?
		$value =~ s/<>/&lt;&gt;/g;

		# â¸çs??
		if ($name eq "message") {
			$value =~ s/\r\n/<br>/g;
			$value =~ s/\n/<br>/g;
			$value =~ s/\r/<br>/g;
		} else {
			$value =~ s/\r//g;
			$value =~ s/\n//g;
		}

		# çÌ?èÓïÒ
		if ($name eq 'del') { push(@DEL,$value); }

		$in{$name} = $value;
	}
	$mode = $in{'mode'};
	$in{'YMD'} =~ s/\D//g;

	# ì˙?ÇÃéÊìæ
	$ENV{'TZ'} = "JST-8";
	($sec,$min,$hour,$mday,$mon,$year,$wday,$dmy) = localtime(time);
	$year += 1900;
	$mon++;

	# ì˙?ÇÃÉtÉHÅ[É}ÉbÉg
	$DATE = sprintf("%04d/%02d/%02d(%s) %02d:%02d",
			$year,$mon,$mday,$week[$wday],$hour,$min);
}


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
body,tr,td,th { font-size:$body_size; line-height: 15pt }
small { font-size:9pt }
A { text-decoration: none; }
a:visited	{color : $vlink_color; text-decoration : none; }
a:active	{color : $alink_color; text-decoration : none; }
a:hover	{color : $hlink_color; text-decoration : underline }
input,textarea{border-left:1px solid $input_border; font-Arial, Helvetica, sans-serif,∑s≤”©˙≈È;
border-right:2px solid $input_border;
border-top:1px solid $input_border;
border-bottom:2px solid $input_border;
background-color : $input_bgcolor; color : $input_color; }
.s{border-left:1px solid $input_border; font-family:∑s≤”©˙≈È;
border-right:2px solid $input_border;
border-top:1px solid $input_border;
border-bottom:2px solid $input_border;
background-color : $input_bgcolor; color : $input_color; }
-->
<!--
BODY {
scrollbar-face-color:#6A9DD0;
scrollbar-highlight-color:#88ABD7;
scrollbar-3dlight-color:#859FCB;
scrollbar-darkshadow-color:#2F3A64;
scrollbar-shadow-color:#4A71B7;
scrollbar-arrow-color:#FFFFFF;
scrollbar-track-color:#3C5E91;
}
-->
</STYLE>
<title>$title</title></head>
<body background="$bg" bgcolor="$bc" text="$tx" link="$lk" vlink="$vl" alink="$al">
EOM
}


sub error {
	&header if (!$head_flag);
	print "<center><h3>ERROR !</h3>\n";
	print "<P><font color=red>$_[0]</font>\n";
	print "</center>\n</body>\n</html>\n";
	exit;
}


sub getweek {
	local($day, $year, $month) = @_;
	# $year  = îN; # 4?
	# $month = ?; # 1-12 --> 1?ÇÕ1

	if ($month == 1 || $month == 2) {
		$year--;
		$month += 12;
	}

	int ($year + int ($year/4) - int ($year/100) + int ($year/400) + int ((13*$month+8)/5) + $day) % 7;
}


sub check {
	&header;
	print "<h2>Check Mode</h2>\n<UL>\n";

	if (-d $logdir) { print "<LI>∞Oø˝¿…≈™®˙!ÅFOK\n"; }
	else { print "<LI>∞Oø˝¿…≈™®˙!ÅFNG Å® $logdir\n"; }

	if (-r $logdir && -w $logdir && -x $logdir) {
		print "<LI>∞Oø˝¿…≈™®˙ÅFOK\n";
	} else {
		print "<LI>∞Oø˝¿…≈™®˙ÅFNG Å® $logdir\n";
	}

	print "</UL>\n</body>\n</html>\n";
	exit;
}