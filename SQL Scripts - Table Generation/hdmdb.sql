USE Master;
GO

IF DB_ID (N'HDM') IS NULL
CREATE DATABASE HDM;
GO

USE HDM
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DayValues]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[DayValues]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[HourValues]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[HourValues]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[MonthValues]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[MonthValues]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[Reduction]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[Reduction]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[CollectionStatus]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[CollectionStatus]
GO


CREATE TABLE [dbo].[DayValues] (
	[ReportIx] [int] NOT NULL ,
	[DateTime] [smalldatetime] NOT NULL ,
	[Value] [float] NULL ,
	[Quality] [int] NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[HourValues] (
	[ReportIx] [int] NOT NULL ,
	[DateTime] [smalldatetime] NOT NULL ,
	[Value] [float] NULL ,
	[Quality] [int] NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[MonthValues] (
	[ReportIx] [int] NOT NULL ,
	[DateTime] [smalldatetime] NOT NULL ,
	[Value] [float] NULL ,
	[Quality] [int] NULL 
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[DayValues] WITH NOCHECK ADD 
	CONSTRAINT [PK_DayValues] PRIMARY KEY  CLUSTERED 
	(
		[DateTime],
		[ReportIx]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[HourValues] WITH NOCHECK ADD 
	CONSTRAINT [PK_HourValues] PRIMARY KEY  CLUSTERED 
	(
		[DateTime],
		[ReportIx]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[MonthValues] WITH NOCHECK ADD 
	CONSTRAINT [PK_MonthValues] PRIMARY KEY  CLUSTERED 
	(
		[DateTime],
		[ReportIx]
	)  ON [PRIMARY] 
GO

CREATE TABLE [dbo].[Reduction](
	[AreaName] [nvarchar](30) NOT NULL,
	[EName] [nvarchar](30) NOT NULL,
	[ReportIx] [int] IDENTITY(1,1) NOT NULL,
	[ReductionMethod] [int] NOT NULL,
	[TransferMethod] [int] NOT NULL,
	[TabIx] [int] NOT NULL,
 CONSTRAINT [PK_Reduction] PRIMARY KEY CLUSTERED 
(
	[AreaName] ASC,
	[EName] ASC,
	[ReductionMethod] ASC,
	[TabIx] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO


CREATE TABLE [dbo].[CollectionStatus](
	[Type] [int] NOT NULL,
	[CollectedUntil] [datetime] NULL,
 CONSTRAINT [PK_CollectionStatus] PRIMARY KEY CLUSTERED 
(
	[Type] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]
GO




