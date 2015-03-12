Action()
{
	int rand_str, i;
	int rand_thinkTime;
	char StrTable[]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
	char targetString[22]="";

	for (i=0; i<26; i++){
		rand_str=rand()%62;
		strncat(targetString, StrTable+rand_str, 1);
	}

	lr_save_string(targetString,"targetString_value");

	lr_start_transaction("Vote");

	web_reg_find("Text=\xCD\xB6\xC6\xB1\xB3\xC9\xB9\xA6!", //投票成功!
		LAST );

	web_add_auto_header("User-Agent", "{UserAgent}");

    web_custom_request("Voting",
        "Method=POST",
        "URL=http://www.4006880288.com/wtg1/mobile/user.php",
        "Body="
			"zpid=38&"
			"opid=owzeBj{targetString_value}&"
			"md_id=70&"
			"act=zuopin_toupiao",
        LAST);

	web_reg_find("Text=\xCD\xB6\xC6\xB1\xB3\xC9\xB9\xA6!", //投票成功!
		LAST );

	web_add_auto_header("User-Agent", "{UserAgent}");

    web_custom_request("VotingOthers",
        "Method=POST",
        "URL=http://www.4006880288.com/wtg1/mobile/user.php",
        "Body=zpid={zpid}&opid=owzeBj{targetString_value}&md_id=70&act=zuopin_toupiao",
        LAST);

	lr_end_transaction("Vote", LR_AUTO);

	rand_thinkTime = 3+ rand()%57;

	lr_think_time(rand_thinkTime);

	return 0;
}
