USE [HDM]
GO

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[CollectionStatus]') AND type in (N'U'))
DROP TABLE [dbo].[CollectionStatus]
GO

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Reduction]') AND type in (N'U'))
DROP TABLE [dbo].[Reduction]
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

