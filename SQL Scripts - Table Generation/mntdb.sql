USE Master;
GO

IF DB_ID (N'MNTDB') IS NULL
CREATE DATABASE MNTDB;
GO


USE MNTDB
GO

CREATE TABLE Changes(
	MntID            int          PRIMARY KEY CLUSTERED,
	Limit            int          DEFAULT 0,
	ResetAcc         bit          DEFAULT 0,
	AddToLimit       int          DEFAULT 0,
	States           int          DEFAULT 0,
	Unit             varchar(16),
	Accumulated      int          DEFAULT 0,
	LastAccumulated  int          DEFAULT 0
)
GO

CREATE TABLE Counter(
	MntID            int          PRIMARY KEY CLUSTERED,
	Limit            float       ,
	AddToLimit       float        ,
	CReset           bit          DEFAULT 0,
	Unit             varchar(50),
	Count            float,
	LastCount        float
)
GO

CREATE TABLE LatestUpdateStamp(
	Count            int          PRIMARY KEY CLUSTERED
)
GO

CREATE TABLE MntElm(
	MntID           int          IDENTITY(1,1),
	Name            varchar(32),
	Area            varchar(32),
	MntType         int          DEFAULT 0,
	JobDesc         varchar(255),
	JobNote         varchar(255),
	VideoFile       varchar(255),
	HlpFile         varchar(255),
	HlpIndex        int          DEFAULT 0,
	AlarmNo         int,          
	NoData          int          DEFAULT 0,
	CompStart       datetime,   
	Measured        datetime,    
	Activated       datetime,               
	Acknowledged    datetime,        
	Completed       datetime,  
	Status          int          DEFAULT 0, 
	JobTitle        varchar(255),    
        MntName         varchar(32),
        MntArea         varchar(32),
        SoonPct         int,
        BindJob         int
	CONSTRAINT MntElm_key PRIMARY KEY CLUSTERED (MntID, Name, Area, MntType)
)
GO

CREATE TABLE Periodical(
          MntID            int          PRIMARY KEY CLUSTERED,
          Limit            int          DEFAULT 0,
          Scale            int          DEFAULT 0
)
GO

CREATE TABLE States(
	MntID            int ,
	State            int          DEFAULT 0
	CONSTRAINT States_key PRIMARY KEY CLUSTERED (MntID, State)
)
GO

CREATE TABLE UsedTime(
	MntID            int          PRIMARY KEY CLUSTERED,
	Limit            int          DEFAULT 0,
	Scale            int          DEFAULT 0,
	ResetAcc         bit          DEFAULT 0,
	AddToLimit       int          DEFAULT 0,
	States           int          DEFAULT 0,
	Unit             varchar(16),     
	Accumulated      int          DEFAULT 0, 
	LastAccumulated  int          DEFAULT 0
);

       