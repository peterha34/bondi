USE Master;
GO

IF DB_ID (N'LOG') IS NULL
CREATE DATABASE LOG;
GO

USE LOG
GO


CREATE TABLE [LOG] (
	[OAN] int NOT NULL,
	[AREA] varchar(255) NOT NULL,
	[ENAME] varchar(255) NOT NULL,
	[ATOM] int NOT NULL,
	[DATE] datetime NOT NULL,
	[MSEC] int NOT NULL,
	[ETYPE] int NOT NULL,
	[DVAL] float NOT NULL,
	[SVAL] varchar(255) NOT NULL,
	[LIMIT] int NOT NULL,
	[STATUS] int NOT NULL,
	[QUALITY] int NOT NULL,
	[OUT] int NOT NULL,
	[IGSSUSER] int NOT NULL
)
GO

ALTER TABLE [LOG] WITH NOCHECK ADD CONSTRAINT [PK_LOG] PRIMARY KEY CLUSTERED(
	[OAN],
	[ATOM],
	[DATE],
	[MSEC]
)
GO


CREATE TABLE [dbo].[ALM](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[PHASE] [int] NOT NULL,
	[OAN] [int] NOT NULL,
	[AREA] [varchar](32) NOT NULL,
	[ENAME] [varchar](32) NOT NULL,
	[ALMNO] [int] NOT NULL,
	[ARR_TIME] [datetime] NULL,
	[ARR_MSEC] [int] NULL,
	[BEG_TIME] [datetime] NULL,
	[BEG_MSEC] [int] NULL,
	[ACK_TIME] [datetime] NULL,
	[ACK_MSEC] [int] NULL,
	[END_TIME] [datetime] NULL,
	[END_MSEC] [int] NULL,
	[ALMSTATE] [int] NOT NULL,
	[MNT] [bit] NOT NULL,
	[WORSTVAL] [float] NULL,
	[DRIVERID] [int] NOT NULL,
	[NODE_NUM] [int] NOT NULL,
	[CODE] [int] NOT NULL,
	[SUBCODE] [int] NOT NULL,
	[BEG_USER_NAME] [varchar](32) NOT NULL,
	[ACK_USER_NAME] [varchar](32) NOT NULL,
	[END_USER_NAME] [varchar](32) NOT NULL,
	[PRIORITY] [int] NOT NULL,
	[ALARM_TEXT] [varchar](255) NOT NULL,
	[OBJ_DESCR] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO




