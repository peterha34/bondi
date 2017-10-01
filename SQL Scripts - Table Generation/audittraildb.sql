USE Master;
GO

IF DB_ID (N'AUDITTRAIL') IS NULL
CREATE DATABASE AUDITTRAIL;
GO

USE AUDITTRAIL;
GO

CREATE TABLE AuditTrail (

	[ID] uniqueidentifier NOT NULL DEFAULT newid(),
	[EventDate] datetime NOT NULL,
	[EventType] int NOT NULL,
	[SubType] int NOT NULL,
	[StationName] varchar(255) NULL,
	[UserName] varchar(255) NULL,
	[Area] varchar(255) NULL,
	[Object] varchar(255) NULL,
	[Atom] int NULL,
	[DValue] float NULL,
	[SValue] varchar(255) NULL,
	[Note] varchar(255) NULL,
	[Comments] varchar(2000) NULL,
	[ApprovedBy] varchar(255) NULL,

	CONSTRAINT [PK_AuditTrail] PRIMARY KEY CLUSTERED ([ID] ASC)
);
GO

CREATE INDEX IDX_AuditTrailDate ON AuditTrail(EventDate);
GO
CREATE INDEX IDX_AuditTrailEventType ON AuditTrail(EventType);
GO
CREATE INDEX IDX_AuditTrailStationName ON AuditTrail(StationName);
GO
CREATE INDEX IDX_AuditTrailUserName ON AuditTrail(UserName);
GO
CREATE INDEX IDX_AuditTrailApprovedBy ON AuditTrail(ApprovedBy);
GO
CREATE INDEX IDX_AuditTrailArea ON AuditTrail(Area);
GO
CREATE INDEX IDX_AuditTrailObject ON AuditTrail(Object);
GO

CREATE TABLE AuditInformation (

	[ID] int NOT NULL,
	[Mark] uniqueidentifier NOT NULL DEFAULT newid(),
	[LastDate] datetime NOT NULL,
	[Version] int NOT NULL

	CONSTRAINT [PK_AuditInformation] PRIMARY KEY CLUSTERED ([ID] ASC)
);
GO

INSERT INTO AuditInformation (ID, Mark, LastDate, Version) VALUES(1, NEWID(), '01-01-1900', 1);
GO
