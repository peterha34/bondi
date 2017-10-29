MODULE SERVER

!////////////////
! Author: MM
!////////////////

VAR socketdev serverSocket;
VAR socketdev clientSocket;
VAR socketdev clientReturnSocket;
PERS string ipController:= "192.168.1.201"; !robot default IP
PERS string piIp:= "192.168.1.5"; !robot default IP
PERS num serverPort:= 5000;
PERS num clientPort:= 8080;



!////////////////////////
!//SERVER: Main procedure
!////////////////////////
PROC main()
    !//Local variables
    VAR string receivedString;   !//Received string
    VAR string sendString;       !//Reply string
    VAR string addString;        !//String to add to the reply.
    VAR bool connected;          !//Client connected
    VAR bool reconnected;        !//Drop and reconnection happened during serving a command
	VAR string returnStr;

	VAR num command;
	
	VAR string clientIP;
	
    TPWrite "SERVER: Server waiting for incoming connections ...";
	returnStr = ""
	WHILE TRUE DO
	    SocketCreate serverSocket;
		SocketBind serverSocket, ipController, serverPort;
		SocketCreate clientSocket;
		SocketBind clientSocket, piIp, clientPort;
		SocketListen serverSocket;
        SocketAccept serverSocket,clientSocket \time;
		SocketReceive client_socket \Str := receivedString \Time:=WAIT_MAX;
		command := StrToVal(receivedString)
		IF command=1 THEN
		!// This is to retrieve the initial treatment tray
			TPWrite "Recieving command: 1"
			returnStr := "1"
		ELSEIF command=2 THEN
		!// This is to return the unsorted tray after allocating discs to sites
			TPWrite "Recieving command: 2"
			returnStr := "2"
		ELSEIF command=3 THEN
			TPWrite "Recieving command: 3"
			returnStr := "3"
		ELSEIF command=4 THEN
			TPWrite "Recieving command: 4"
			returnStr := "4"
		ELSEIF command=5 THEN
			TPWrite "Recieving command: 5"
			returnStr := "5"
		ELSEIF command=6 THEN
			TPWrite "Recieving command: 6"
			returnStr := "6"
		ELSEIF command=7 THEN
			TPWrite "Recieving command: 7"
			returnStr := "7"
		ELSEIF command=8 THEN
			TPWrite "Recieving command: 8"
			returnStr := "8"
		ELSEIF command=9 THEN
			TPWrite "Recieving command: 9"
			returnStr := "9"
		ELSEIF command=10 THEN
			TPWrite "Recieving command: 10"
			returnStr := "10"
		ELSEIF command=11 THEN
		!// Disc 1 to treatment site 1
			TPWrite "Recieving command: 11"
			returnStr := "11"
		ELSEIF command=12 THEN
		!// Disc 2 to treatment site 1
			TPWrite "Recieving command: 12"
			returnStr := "12"
		ELSEIF command=13 THEN
		!// Disc 3 to treatment site 1
			TPWrite "Recieving command: 13"
			returnStr := "13"
		ELSEIF command=14 THEN
		!// Disc 4 to treatment site 1
			TPWrite "Recieving command: 14"
			returnStr := "14"
		ELSEIF command=15 THEN
		!// Disc 5 to treatment site 1
			TPWrite "Recieving command: 15"
			returnStr := "15"
		ELSEIF command=16 THEN
		!// Disc 6 to treatment site 1
			TPWrite "Recieving command: 16"
			returnStr := "16"
		ELSEIF command=17 THEN
		!// Disc 7 to treatment site 1
			TPWrite "Recieving command: 17"
			returnStr := "17"
		ELSEIF command=18 THEN
		!// Disc 8 to treatment site 1
			TPWrite "Recieving command: 18"
			returnStr := "18"
		ELSEIF command=21 THEN
		!// Disc 1 to treatment site 2
			TPWrite "Recieving command: 21"
			returnStr := "21"
		ELSEIF command=22 THEN
		!// Disc 2 to treatment site 2
			TPWrite "Recieving command: 22"
			returnStr := "22"
		ELSEIF command=23 THEN
		!// Disc 3 to treatment site 2
			TPWrite "Recieving command: 23"
			returnStr := "23"
		ELSEIF command=24 THEN
		!// Disc 4 to treatment site 2
			TPWrite "Recieving command: 24"
			returnStr := "24"
		ELSEIF command=25 THEN
		!// Disc 5 to treatment site 2
			TPWrite "Recieving command: 25"
			returnStr := "25"	
		ELSEIF command=26 THEN
		!// Disc 6 to treatment site 2
			TPWrite "Recieving command: 26"
			returnStr := "26"	
		ELSEIF command=27 THEN
		!// Disc 7 to treatment site 2
			TPWrite "Recieving command: 27"
			returnStr := "27"	
		ELSEIF command=28 THEN
		!// Disc 8 to treatment site 2
			TPWrite "Recieving command: 28"
			returnStr := "28"
		ELSEIF command=31 THEN
		!// Disc 1 to treatment site 3
			TPWrite "Recieving command: 31"
			returnStr := "31"	
		ELSEIF command=32 THEN
		!// Disc 2 to treatment site 3
			TPWrite "Recieving command: 32"
			returnStr := "32"	
		ELSEIF command=33 THEN
		!// Disc 3 to treatment site 3
			TPWrite "Recieving command: 33"
			returnStr := "33"
		ELSEIF command=34 THEN
		!// Disc 4 to treatment site 3
			TPWrite "Recieving command: 34"
			returnStr := "34"	
		ELSEIF command=35 THEN
		!// Disc 5 to treatment site 3
			TPWrite "Recieving command: 35"
			returnStr := "35"	
		ELSEIF command=36 THEN
		!// Disc 6 to treatment site 3
			TPWrite "Recieving command: 36"
			returnStr := "36"
		ELSEIF command=37 THEN
		!// Disc 7 to treatment site 3
			TPWrite "Recieving command: 37"
			returnStr := "37"
		ELSEIF command=38 THEN
		!// Disc 8 to treatment site 3
			TPWrite "Recieving command: 38"
			returnStr := "38"		
		ELSEIF command=38 THEN
		!// Disc 8 to treatment site 3
			TPWrite "Recieving command: 38"
			returnStr := "38"	
		ELSEIF command=411 THEN
		!// Treatment site 1 to tray slot 1, height offest of 1 disc
			TPWrite "Recieving command: 41"
			returnStr := "411"	
		ELSEIF command=412 THEN
		!// Treatment site 1 to tray slot 1, height offest of 2 disc
			TPWrite "Recieving command: 42"
			returnStr := "412"	
		ELSEIF command=413 THEN
		!// Treatment site 1 to tray slot 1, height offest of 3 disc
			TPWrite "Recieving command: 413"
			returnStr := "413"	
		ELSEIF command=421 THEN
		!// Treatment site 1 to tray slot 2, height offest of 1 disc
			TPWrite "Recieving command: 421"
			returnStr := "421"	
		ELSEIF command=422 THEN
		!// Treatment site 1 to tray slot 2, height offest of 2 disc
			TPWrite "Recieving command: 422"
			returnStr := "422"	
		ELSEIF command=423 THEN
		!// Treatment site 1 to tray slot 2, height offest of 3 disc
			TPWrite "Recieving command: 423"
			returnStr := "423"		
		ELSEIF command=431 THEN
		!// Treatment site 1 to tray slot 3, height offest of 1 disc
			TPWrite "Recieving command: 431"
			returnStr := "431"	
		ELSEIF command=432 THEN
		!// Treatment site 1 to tray slot 3, height offest of 2 disc
			TPWrite "Recieving command: 432"
			returnStr := "432"	
		ELSEIF command=433 THEN
		!// Treatment site 1 to tray slot 3, height offest of 3 disc
			TPWrite "Recieving command: 433"
			returnStr := "433"		
		ELSEIF command=441 THEN
		!// Treatment site 1 to tray slot 4, height offest of 1 disc
			TPWrite "Recieving command: 441"
			returnStr := "441"	
		ELSEIF command=442 THEN
		!// Treatment site 1 to tray slot 4, height offest of 2 disc
			TPWrite "Recieving command: 442"
			returnStr := "442"	
		ELSEIF command=443 THEN
		!// Treatment site 1 to tray slot 4, height offest of 3 disc
			TPWrite "Recieving command: 443"
			returnStr := "443"	
		ELSEIF command=451 THEN
		!// Treatment site 1 to tray slot 5, height offest of 1 disc
			TPWrite "Recieving command: 451"
			returnStr := "451"	
		ELSEIF command=452 THEN
		!// Treatment site 1 to tray slot 5, height offest of 2 disc
			TPWrite "Recieving command: 452"
			returnStr := "452"	
		ELSEIF command=453 THEN
		!// Treatment site 1 to tray slot 5, height offest of 3 disc
			TPWrite "Recieving command: 453"
			returnStr := "453"	
		ELSEIF command=461 THEN
		!// Treatment site 1 to tray slot 6, height offest of 1 disc
			TPWrite "Recieving command: 461"
			returnStr := "461"	
		ELSEIF command=462 THEN
		!// Treatment site 1 to tray slot 6, height offest of 2 disc
			TPWrite "Recieving command: 462"
			returnStr := "462"	
		ELSEIF command=463 THEN
		!// Treatment site 1 to tray slot 6, height offest of 3 disc
			TPWrite "Recieving command: 463"
			returnStr := "463"
		ELSEIF command=471 THEN
		!// Treatment site 1 to tray slot 7, height offest of 1 disc
			TPWrite "Recieving command: 471"
			returnStr := "471"
		ELSEIF command=472 THEN
		!// Treatment site 1 to tray slot 7, height offest of 2 disc
			TPWrite "Recieving command: 472"
			returnStr := "472"
		ELSEIF command=473 THEN	
		!// Treatment site 1 to tray slot 7, height offest of 3 disc		
			TPWrite "Recieving command: 473"
			returnStr := "473"
		ELSEIF command=481 THEN
		!// Treatment site 1 to tray slot 8, height offest of 1 disc
			TPWrite "Recieving command: 481"
			returnStr := "481"
		ELSEIF command=482 THEN
		!// Treatment site 1 to tray slot 8, height offest of 2 disc
			TPWrite "Recieving command: 482"
			returnStr := "482"
		ELSEIF command=483 THEN	
		!// Treatment site 1 to tray slot 8, height offest of 3 disc
			TPWrite "Recieving command: 483"
			returnStr := "483"
		ELSEIF command=491 THEN
		!// Treatment site 1 to tray slot 9, height offest of 1 disc
			TPWrite "Recieving command: 491"
			returnStr := "491"
		ELSEIF command=492 THEN
		!// Treatment site 1 to tray slot 9, height offest of 2 disc
			TPWrite "Recieving command: 492"
			returnStr := "492"
		ELSEIF command=493 THEN	
		!// Treatment site 1 to tray slot 9, height offest of 3 disc
			TPWrite "Recieving command: 493"
			returnStr := "493"
		ELSEIF command=511 THEN
		!// Treatment site 2 to tray slot 1, height offest of 1 disc
			TPWrite "Recieving command: 511"
			returnStr := "511"
		ELSEIF command=512 THEN
		!// Treatment site 2 to tray slot 1, height offest of 2 disc
			TPWrite "Recieving command: 512"
			returnStr := "512"
		ELSEIF command=513 THEN	
		!// Treatment site 2 to tray slot 1, height offest of 3 disc
			TPWrite "Recieving command: 513"
			returnStr := "513"
		ELSEIF command=521 THEN
		!// Treatment site 2 to tray slot 2, height offest of 1 disc
			TPWrite "Recieving command: 521"
			returnStr := "521"
		ELSEIF command=522 THEN
		!// Treatment site 2 to tray slot 2, height offest of 2 disc
			TPWrite "Recieving command: 522"
			returnStr := "522"
		ELSEIF command=523 THEN
		!// Treatment site 2 to tray slot 2, height offest of 3 disc
			TPWrite "Recieving command: 523"
			returnStr := "523"
		ELSEIF command=531 THEN
		!// Treatment site 2 to tray slot 3, height offest of 1 disc
			TPWrite "Recieving command: 531"
			returnStr := "531"
		ELSEIF command=532 THEN
		!// Treatment site 2 to tray slot 3, height offest of 2 disc
			TPWrite "Recieving command: 532"
			returnStr := "532"
		ELSEIF command=533 THEN	
		!// Treatment site 2 to tray slot 3, height offest of 3 disc
			TPWrite "Recieving command: 533"
			returnStr := "533"
		ELSEIF command=541 THEN
		!// Treatment site 2 to tray slot 4, height offest of 1 disc
			TPWrite "Recieving command: 541"
			returnStr := "541"
		ELSEIF command=542 THEN
		!// Treatment site 2 to tray slot 4, height offest of 2 disc
			TPWrite "Recieving command: 542"
			returnStr := "542"
		ELSEIF command=543 THEN	
		!// Treatment site 2 to tray slot 4, height offest of 3 disc
			TPWrite "Recieving command: 543"
			returnStr := "543"
		ELSEIF command=551 THEN
		!// Treatment site 2 to tray slot 5, height offest of 1 disc
			TPWrite "Recieving command: 551"
			returnStr := "551"
		ELSEIF command=552 THEN
		!// Treatment site 2 to tray slot 5, height offest of 2 disc
			TPWrite "Recieving command: 552"
			returnStr := "552"
		ELSEIF command=553 THEN				
		!// Treatment site 2 to tray slot 5, height offest of 3 disc
			TPWrite "Recieving command: 553"
			returnStr := "553"
		ELSEIF command=561 THEN
		!// Treatment site 2 to tray slot 6, height offest of 1 disc
			TPWrite "Recieving command: 561"
			returnStr := "561"
		ELSEIF command=562 THEN
		!// Treatment site 2 to tray slot 6, height offest of 2 disc
			TPWrite "Recieving command: 562"
			returnStr := "562"
		ELSEIF command=563 THEN
		!// Treatment site 2 to tray slot 6, height offest of 3 disc
			TPWrite "Recieving command: 563"
			returnStr := "563"
		ELSEIF command=571 THEN
		!// Treatment site 2 to tray slot 7, height offest of 1 disc
			TPWrite "Recieving command: 571"
			returnStr := "571"
		ELSEIF command=572 THEN
		!// Treatment site 2 to tray slot 7, height offest of 2 disc
			TPWrite "Recieving command: 572"
			returnStr := "572"
		ELSEIF command=573 THEN			
		!// Treatment site 2 to tray slot 7, height offest of 3 disc
			TPWrite "Recieving command: 573"
			returnStr := "573"
		ELSEIF command=581 THEN
		!// Treatment site 2 to tray slot 8, height offest of 1 disc
			TPWrite "Recieving command: 581"
			returnStr := "581"
		ELSEIF command=582 THEN
		!// Treatment site 2 to tray slot 8, height offest of 2 disc
			TPWrite "Recieving command: 582"
			returnStr := "582"
		ELSEIF command=583 THEN	
		!// Treatment site 2 to tray slot 8, height offest of 3 disc		
			TPWrite "Recieving command: 583"
			returnStr := "583"
		ELSEIF command=591 THEN
		!// Treatment site 2 to tray slot 9, height offest of 1 disc
			TPWrite "Recieving command: 591"
			returnStr := "591"
		ELSEIF command=592 THEN
		!// Treatment site 2 to tray slot 9, height offest of 2 disc
			TPWrite "Recieving command: 592"
			returnStr := "592"
		ELSEIF command=593 THEN	
		!// Treatment site 2 to tray slot 9, height offest of 3 disc
			TPWrite "Recieving command: 593"
			returnStr := "593"
		ELSEIF command=611 THEN
		!// Treatment site 3 to tray slot 1, height offest of 1 disc
			TPWrite "Recieving command: 611"
			returnStr := "611"
		ELSEIF command=612 THEN
		!// Treatment site 3 to tray slot 1, height offest of 2 disc
			TPWrite "Recieving command: 612"
			returnStr := "612"
		ELSEIF command=613 THEN	
		!// Treatment site 3 to tray slot 1, height offest of 3 disc
			TPWrite "Recieving command: 613"
			returnStr := "613"
		ELSEIF command=621 THEN
		!// Treatment site 3 to tray slot 2, height offest of 1 disc
			TPWrite "Recieving command: 621"
			returnStr := "621"
		ELSEIF command=622 THEN
		!// Treatment site 3 to tray slot 2, height offest of 2 disc
			TPWrite "Recieving command: 622"
			returnStr := "622"
		ELSEIF command=623 THEN			
		!// Treatment site 3 to tray slot 2, height offest of 3 disc
			TPWrite "Recieving command: 623"
			returnStr := "623"
		ELSEIF command=631 THEN
		!// Treatment site 3 to tray slot 3, height offest of 1 disc
			TPWrite "Recieving command: 631"
			returnStr := "631"
		ELSEIF command=632 THEN
		!// Treatment site 3 to tray slot 3, height offest of 2 disc
			TPWrite "Recieving command: 632"
			returnStr := "632"
		ELSEIF command=633 THEN	
		!// Treatment site 3 to tray slot 3, height offest of 3 disc
			TPWrite "Recieving command: 633"
			returnStr := "633"
		ELSEIF command=641 THEN
		!// Treatment site 3 to tray slot 4, height offest of 1 disc
			TPWrite "Recieving command: 641"
			returnStr := "641"
		ELSEIF command=642 THEN
		!// Treatment site 3 to tray slot 4, height offest of 2 disc
			TPWrite "Recieving command: 642"
			returnStr := "642"
		ELSEIF command=643 THEN	
		!// Treatment site 3 to tray slot 4, height offest of 3 disc
			TPWrite "Recieving command: 643"
			returnStr := "643"
		ELSEIF command=651 THEN
		!// Treatment site 3 to tray slot 5, height offest of 1 disc
			TPWrite "Recieving command: 651"
			returnStr := "651"
		ELSEIF command=652 THEN
		!// Treatment site 3 to tray slot 5, height offest of 2 disc
			TPWrite "Recieving command: 652"
			returnStr := "652"
		ELSEIF command=653 THEN				
		!// Treatment site 3 to tray slot 5, height offest of 3 disc
			TPWrite "Recieving command: 653"
			returnStr := "653"
		ELSEIF command=661 THEN
		!// Treatment site 3 to tray slot 6, height offest of 1 disc
			TPWrite "Recieving command: 661"
			returnStr := "661"
		ELSEIF command=662 THEN
		!// Treatment site 3 to tray slot 6, height offest of 2 disc
			TPWrite "Recieving command: 662"
			returnStr := "662"
		ELSEIF command=663 THEN
		!// Treatment site 3 to tray slot 6, height offest of 3 disc
			TPWrite "Recieving command: 663"
			returnStr := "663"
		ELSEIF command=671 THEN
		!// Treatment site 3 to tray slot 7, height offest of 1 disc
			TPWrite "Recieving command: 671"
			returnStr := "671"
		ELSEIF command=672 THEN
		!// Treatment site 3 to tray slot 7, height offest of 2 disc
			TPWrite "Recieving command: 672"
			returnStr := "672"
		ELSEIF command=673 THEN			
		!// Treatment site 3 to tray slot 7, height offest of 3 disc
			TPWrite "Recieving command: 673"
			returnStr := "673"
		ELSEIF command=681 THEN
		!// Treatment site 3 to tray slot 8, height offest of 1 disc
			TPWrite "Recieving command: 681"
			returnStr := "681"
		ELSEIF command=682 THEN
		!// Treatment site 3 to tray slot 8, height offest of 2 disc
			TPWrite "Recieving command: 682"
			returnStr := "682"
		ELSEIF command=683 THEN		
		!// Treatment site 3 to tray slot 8, height offest of 3 disc
			TPWrite "Recieving command: 683"
			returnStr := "683"	
		ELSEIF command=691 THEN
		!// Treatment site 3 to tray slot 9, height offest of 1 disc
			TPWrite "Recieving command: 691"
			returnStr := "691"
		ELSEIF command=692 THEN
		!// Treatment site 3 to tray slot 9, height offest of 2 disc
			TPWrite "Recieving command: 692"
			returnStr := "692"
		ELSEIF command=693 THEN					
		!// Treatment site 3 to tray slot 9, height offest of 3 disc
			TPWrite "Recieving command: 693"
			returnStr := "693"
		ELSE
		!// Treatment site ? to tray slot ?, height offset of ? disc
			TPWrite "Unrecognised command"
		ENDIF
		
		SocketClose clientSocket;
        SocketCreate clientReturnSocket;
        SocketConnect clientReturnSocket, piIp, clientPort;
		SocketSend clientSocket \Str := "LOADER_ROBOT_DATA:"+returnStr;
		SocketClose clientReturnSocket;
    ENDWHILE
ENDPROC
ENDMODULE