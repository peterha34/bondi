MODULE SERVER

!////////////////
! Author: MM
!////////////////

VAR socketdev serverSocket;
VAR socketdev clientSocket;
VAR socketdev clientReturnSocket;
PERS string ipController:= "192.168.1.200"; !robot default IP
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
		ENDIF
		
		SocketClose clientSocket;
        SocketCreate clientReturnSocket;
        SocketConnect clientReturnSocket, piIp, clientPort;
		SocketSend clientSocket \Str := "LOADER_ROBOT_DATA:"+returnStr;
		SocketClose clientReturnSocket;
    ENDWHILE
ENDPROC
ENDMODULE