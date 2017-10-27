MODULE MainModule
	CONST robtarget home:=[[403.82,14.15,346.27],[0.0493407,-0.0813297,0.995449,0.00562966],[0,0,3,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget tray1:=[[420.60,-166.92,132.13],[0.0493325,-0.0813363,0.995449,0.00563245],[-1,0,3,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget tray11:=[[420.92,-167.05,265.92],[0.051019,-0.081307,0.995371,0.00472304],[-1,0,3,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget tray21:=[[447.27,165.59,265.91],[0.0510026,-0.081334,0.99537,0.00470602],[0,-1,4,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget tray31:=[[447.26,165.59,201.34],[0.0509971,-0.0813541,0.995369,0.00470527],[0,-1,4,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	CONST robtarget tray41:=[[447.26,165.58,189.04],[0.0509729,-0.0813178,0.995373,0.0047083],[0,-1,4,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
	PROC main()
		MoveL home, v100, z50, tool0;
		MoveL tray11, v100, z50, tool0;
		MoveL tray1, v100, z50, tool0;
		WaitTime reg1;
		Set DO10_6;
		WaitTime reg1;
		MoveL tray11, v100, z50, tool0;
		MoveL tray21, v100, z50, tool0;
		MoveL tray41, v100, z50, tool0;
		WaitTime reg1;
		Reset DO10_6;
		WaitTime reg1;
		MoveL tray21, v100, z50, tool0;
		MoveL home, v100, z50, tool0;
	ENDPROC
ENDMODULE