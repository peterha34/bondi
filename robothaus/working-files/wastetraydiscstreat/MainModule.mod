MODULE MainModule
	CONST robtarget homeloader:=[[404.50,-178.17,361.47],[0.00111974,-0.99664,-0.0504217,0.0645445],[-1,-1,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget homeloader10:=[[411.51,-168.16,275.07],[0.00115634,-0.996636,-0.0504437,0.0645857],[-1,-1,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget wasteTraylifted:=[[411.51,-168.16,275.07],[0.00115634,-0.996636,-0.0504437,0.0645857],[-1,-1,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget homeloader20:=[[411.29,-167.96,135.06],[0.00117571,-0.996634,-0.0504923,0.06458],[-1,-1,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget wasteTray:=[[411.29,-167.96,135.06],[0.00117417,-0.996633,-0.0504946,0.0645806],[-1,-1,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget aboveConveyor:=[[439.72,160.85,283.16],[0.0012462,-0.996619,-0.0505143,0.0647929],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget wasteTraydrop:=[[436.40,164.87,198.98],[0.00126291,-0.996622,-0.050467,0.0647741],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	
	
	CONST robtarget homeloader30:=[[391.27,123.77,206.04],[0.00112019,-0.996638,-0.0504361,0.0645558],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget homeloader40:=[[391.27,123.78,315.76],[0.001122,-0.996636,-0.0504671,0.0645596],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget homeloader50:=[[394.54,209.44,207.75],[0.00117728,-0.996613,-0.0504926,0.0649032],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	

	CONST robtarget disc1:=[[394.54,209.43,207.74],[0.00117305,-0.996612,-0.050504,0.0649083],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc11:=[[394.54,209.43,290.15],[0.00115452,-0.996609,-0.0505421,0.0649249],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc21:=[[439.88,209.57,288.92],[0.00116209,-0.996608,-0.0505461,0.064927],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc22:=[[440.21,209.58,205.60],[0.00117536,-0.996611,-0.0505139,0.0649168],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc32:=[[486.08,213.23,284.52],[0.00119247,-0.996608,-0.0504689,0.0649902],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc41:=[[483.76,211.69,206.62],[0.00118804,-0.99661,-0.050451,0.0649767],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc42:=[[488.17,167.03,304.25],[0.00116235,-0.99661,-0.0504316,0.0649985],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc51:=[[488.17,167.03,304.25],[0.00116235,-0.99661,-0.0504316,0.0649985],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc52:=[[483.03,164.28,207.30],[0.00115694,-0.996605,-0.0504642,0.0650398],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc61:=[[396.27,124.78,300.76],[0.001122,-0.996636,-0.0504671,0.0645596],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc62:=[[396.27,124.77,206.04],[0.00112019,-0.996638,-0.0504361,0.0645558],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc71:=[[442.62,130.57,295.45],[0.00115495,-0.9966,-0.0504936,0.0650958],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc72:=[[437.52,120.47,206.84],[0.00117387,-0.996601,-0.0504666,0.0651017],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc81:=[[483.03,131.46,281.90],[0.00113903,-0.9966,-0.0504776,0.0651036],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget disc82:=[[482.92,118.25,207.45],[0.0011428,-0.996601,-0.0504692,0.0650994],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];




	CONST robtarget treat1:=[[75.01,218.78,271.24],[0.00116703,-0.996604,-0.0503811,0.0651189],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget treat11:=[[75.01,209.90,169.11],[0.00116605,-0.996602,-0.0503953,0.0651359],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget treat21:=[[75.43,266.88,258.16],[0.00115585,-0.996604,-0.0503577,0.0651408],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	
	CONST robtarget treat22:=[[73.60,265.05,171.73],[0.00114626,-0.996605,-0.0503423,0.0651315],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	
	CONST robtarget treat3:=[[73.60,324.88,249.29],[0.00113629,-0.996606,-0.0503248,0.0651353],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget treat33:=[[73.60,318.91,171.08],[0.00113964,-0.996606,-0.0503389,0.0651187],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	
	PROC main()
		MoveL homeloader, v100, z50, tool0;
		MoveL wasteTray, v100, z50, tool0;
		WaitTime reg1;
		Set DO10_6;
		WaitTime reg1;
		MoveL wasteTraylifted, v100, z50, tool0;
		MoveL aboveConveyor, v100, z50, tool0;
		MoveL wasteTraydrop, v100, z50, tool0;
		WaitTime reg1;
		Reset DO10_6;
		WaitTime reg1;
		MoveL aboveConveyor, v100, z50, tool0;
		MoveL homeloader, v100, z50, tool0;
		
		
		
		
		MoveL homeloader30, v100, z50, tool0;
		WaitTime reg1;
		Set DO10_6;
		WaitTime reg1;
		MoveL homeloader40, v100, z50, tool0;
		WaitTime reg1;
		Set DO10_6;
		WaitTime reg1;

		MoveL disc1, v100, z50, tool0;
		MoveL disc11, v100, z50, tool0;
		WaitTime reg1;
		Set DO10_6;
		WaitTime reg1;
		WaitTime reg1;
		Reset DO10_6;
		WaitTime reg1;
		MoveL disc21, v100, z50, tool0;
		MoveL disc22, v100, z50, tool0;
		MoveL disc31, v100, z50, tool0;
		MoveL disc32, v100, z50, tool0;
		MoveL disc51, v100, z50, tool0;
		MoveL disc52, v100, z50, tool0;
		MoveL disc81, v100, z50, tool0;
		MoveL disc82, v100, z50, tool0;
		MoveL disc71, v100, z50, tool0;
		MoveL disc72, v100, z50, tool0;
		MoveL treat1, v100, z50, tool0;
		MoveL treat11, v100, z50, tool0;
		MoveL treat21, v100, z50, tool0;
		MoveL treat22, v100, z50, tool0;
		MoveL treat3, v100, z50, tool0;
		MoveL treat33, v100, z50, tool0;
	ENDPROC
ENDMODULE