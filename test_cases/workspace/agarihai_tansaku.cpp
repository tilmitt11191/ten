/メンツ抜き出し関数
void KiriwakeNukidasi()
{
	int i;
	for(i=0;i<38;i++){
	for(;!tehai[i];i++);
	if(i>=38){
		if(kiriwake[9]!=0){//４メンツ１頭とれてるなら
		/********************************/
		/* ここで切り分けが終わります　　*/
		/* ここから符計算等に入ります　　*/
		/* 構成が関係する役はメンツごと　*/
		/* にここで判定すること　　　　　*/
		/********************************/
		}
	return;
	}
	//アンコ抜き出し
	if(tehai[i] >=3){
		tehai[i] -=3;
		//ロンのあがり牌ならミンコウである
		if(i==agarihai&& ron==true){
			kiriwake[p_kiriwake]=PON;
		}
		else{
			kiriwake[p_kiriwake]=ANKO;
		}
		kiriwake[p_kiriwake+1] =i,p_kiriwake+=2;
		KiriwakeNukidasi();//再帰
		p_kiriwake-=2,kiriwake[p_kiriwake]=0,kiriwake[p_kiriwake+1]=0;
		tehai[i] += 3;
	}
	//シュンツ抜き出し
	if(tehai[i] && tehai[i+1] && tehai[i+2] &&i<30){
		tehai[i]--,tehai[i+1]--,tehai[i+2]--;
		kiriwake[p_kiriwake]=SYUNTU,kiriwake[p_kiriwake+1] =i,p_kiriwake+=2;
 		KiriwakeNukidasi();//再帰
		p_kiriwake-=2,kiriwake[p_kiriwake]=0,kiriwake[p_kiriwake+1]=0;
		tehai[i]++,tehai[i+1]++,tehai[i+2]++;
		}	            
	}
}