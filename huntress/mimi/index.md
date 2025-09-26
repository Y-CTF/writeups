+++
title = "Mimi"
description = "Uh oh! Mimi forgot her password for her Windows laptop!\n\nLuckily, she dumped one of the crucial processes running on her computer (don't ask me why, okay)... can you help her recover her password?\n\nNOTE: Archive password is mimi"
authors = ["mango", "Ary.eth"]
date = 2024-09-30

[taxonomies]
categories = ["warmups"]
+++

## Description

Uh oh! Mimi forgot her password for her Windows laptop!

Luckily, she dumped one of the crucial processes running on her computer (don't ask me why, okay)... can you help her recover her password?

NOTE: Archive password is mimi

----

Using the `minidump` python library we can dump the following:

```
== Minidump File ==
== MinidumpHeader ==
Signature: PMDM
Version: 42899
ImplementationVersion: 41053
NumberOfStreams: 18
StreamDirectoryRva: 32
CheckSum: 0
Reserved: 1725935602
TimeDateStamp: 4593702
Flags: 0
== System Info ==
ProcessorArchitecture PROCESSOR_ARCHITECTURE.AMD64
OperatingSystem -guess- Windows 11 - 22H2
ProcessorLevel 23
ProcessorRevision 0x3100
NumberOfProcessors 4
ProductType PRODUCT_TYPE.VER_NT_WORKSTATION
MajorVersion 10
MinorVersion 0
BuildNumber 22621
PlatformId PLATFORM_ID.VER_PLATFORM_WIN32_NT
CSDVersion: 
SuiteMask 256
VendorId 
VersionInformation None
FeatureInformation None
AMDExtendedCpuFeatures None
ProcessorFeatures 0x1f310e2774c 0x0
StreamType: MINIDUMP_STREAM_TYPE.ThreadListStream Size: 532 File offset: 1668
StreamType: MINIDUMP_STREAM_TYPE.ThreadInfoListStream Size: 716 File offset: 2200
StreamType: MINIDUMP_STREAM_TYPE.ModuleListStream Size: 9616 File offset: 2916
StreamType: MINIDUMP_STREAM_TYPE.UnloadedModuleListStream Size: 60 File offset: 12532
StreamType: MINIDUMP_STREAM_TYPE.TokenStream Size: 704 File offset: 12592
StreamType: MINIDUMP_STREAM_TYPE.Memory64ListStream Size: 9392 File offset: 200717
StreamType: MINIDUMP_STREAM_TYPE.MemoryInfoListStream Size: 39376 File offset: 161341
StreamType: MINIDUMP_STREAM_TYPE.SystemInfoStream Size: 56 File offset: 248
StreamType: MINIDUMP_STREAM_TYPE.MiscInfoStream Size: 1364 File offset: 304
StreamType: MINIDUMP_STREAM_TYPE.HandleDataStream Size: 58896 File offset: 102445
StreamType: MINIDUMP_STREAM_TYPE.SystemMemoryInfoStream Size: 492 File offset: 13296
StreamType: MINIDUMP_STREAM_TYPE.ProcessVmCountersStream Size: 152 File offset: 13788
StreamType: MINIDUMP_STREAM_TYPE.CommentStreamW Size: 240 File offset: 36945
StreamType: MINIDUMP_STREAM_TYPE.UnusedStream Size: 0 File offset: 0
StreamType: MINIDUMP_STREAM_TYPE.UnusedStream Size: 0 File offset: 0
StreamType: MINIDUMP_STREAM_TYPE.UnusedStream Size: 0 File offset: 0
StreamType: MINIDUMP_STREAM_TYPE.UnusedStream Size: 0 File offset: 0
StreamType: MINIDUMP_STREAM_TYPE.UnusedStream Size: 0 File offset: 0
Module name: C:\Windows\System32\lsass.exe BaseAddress: 0x7ff61b8f0000 Size: 0x12000 Endaddress: 0x7ff61b902000
Module name: C:\Windows\System32\ntdll.dll BaseAddress: 0x7ffa34bd0000 Size: 0x217000 Endaddress: 0x7ffa34de7000
Module name: C:\Windows\System32\kernel32.dll BaseAddress: 0x7ffa34490000 Size: 0xc4000 Endaddress: 0x7ffa34554000
Module name: C:\Windows\System32\KERNELBASE.dll BaseAddress: 0x7ffa322f0000 Size: 0x3ad000 Endaddress: 0x7ffa3269d000
Module name: C:\Windows\System32\rpcrt4.dll BaseAddress: 0x7ffa33430000 Size: 0x114000 Endaddress: 0x7ffa33544000
Module name: C:\Windows\System32\lsasrv.dll BaseAddress: 0x7ffa31900000 Size: 0x195000 Endaddress: 0x7ffa31a95000
Module name: C:\Windows\System32\ucrtbase.dll BaseAddress: 0x7ffa31fc0000 Size: 0x111000 Endaddress: 0x7ffa320d1000
Module name: C:\Windows\System32\msvcp_win.dll BaseAddress: 0x7ffa320e0000 Size: 0x9a000 Endaddress: 0x7ffa3217a000
Module name: C:\Windows\System32\lsaadt.dll BaseAddress: 0x7ffa318c0000 Size: 0x34000 Endaddress: 0x7ffa318f4000
Module name: C:\Windows\System32\sechost.dll BaseAddress: 0x7ffa346f0000 Size: 0xa9000 Endaddress: 0x7ffa34799000
Module name: C:\Windows\System32\bcrypt.dll BaseAddress: 0x7ffa32710000 Size: 0x28000 Endaddress: 0x7ffa32738000
Module name: C:\Windows\System32\samsrv.dll BaseAddress: 0x7ffa317d0000 Size: 0xef000 Endaddress: 0x7ffa318bf000
Module name: C:\Windows\System32\crypt32.dll BaseAddress: 0x7ffa32180000 Size: 0x167000 Endaddress: 0x7ffa322e7000
Module name: C:\Windows\System32\ncrypt.dll BaseAddress: 0x7ffa317a0000 Size: 0x2e000 Endaddress: 0x7ffa317ce000
Module name: C:\Windows\System32\ntasn1.dll BaseAddress: 0x7ffa31760000 Size: 0x37000 Endaddress: 0x7ffa31797000
Module name: C:\Windows\System32\msasn1.dll BaseAddress: 0x7ffa31aa0000 Size: 0x12000 Endaddress: 0x7ffa31ab2000
Module name: C:\Windows\System32\vbsapi.dll BaseAddress: 0x7ffa31730000 Size: 0x2d000 Endaddress: 0x7ffa3175d000
Module name: C:\Windows\System32\msvcrt.dll BaseAddress: 0x7ffa34140000 Size: 0xa7000 Endaddress: 0x7ffa341e7000
Module name: C:\Windows\System32\advapi32.dll BaseAddress: 0x7ffa34630000 Size: 0xb2000 Endaddress: 0x7ffa346e2000
Module name: C:\Windows\System32\bcd.dll BaseAddress: 0x7ffa31700000 Size: 0x23000 Endaddress: 0x7ffa31723000
Module name: C:\Windows\System32\wldp.dll BaseAddress: 0x7ffa316b0000 Size: 0x49000 Endaddress: 0x7ffa316f9000
Module name: C:\Windows\System32\combase.dll BaseAddress: 0x7ffa347a0000 Size: 0x388000 Endaddress: 0x7ffa34b28000
Module name: C:\Windows\System32\oleaut32.dll BaseAddress: 0x7ffa343b0000 Size: 0xd7000 Endaddress: 0x7ffa34487000
Module name: C:\Windows\System32\bcryptprimitives.dll BaseAddress: 0x7ffa32890000 Size: 0x7b000 Endaddress: 0x7ffa3290b000
Module name: C:\Windows\System32\msprivs.dll BaseAddress: 0x1dcaf3d0000 Size: 0x3000 Endaddress: 0x1dcaf3d3000
Module name: C:\Windows\System32\netprovfw.dll BaseAddress: 0x7ffa31690000 Size: 0x16000 Endaddress: 0x7ffa316a6000
Module name: C:\Windows\System32\joinutil.dll BaseAddress: 0x7ffa31660000 Size: 0x2c000 Endaddress: 0x7ffa3168c000
Module name: C:\Windows\System32\negoexts.dll BaseAddress: 0x7ffa31630000 Size: 0x26000 Endaddress: 0x7ffa31656000
Module name: C:\Windows\System32\cryptsp.dll BaseAddress: 0x7ffa31610000 Size: 0x1b000 Endaddress: 0x7ffa3162b000
Module name: C:\Windows\System32\CRYPTBASE.dll BaseAddress: 0x7ffa31600000 Size: 0xc000 Endaddress: 0x7ffa3160c000
Module name: C:\Windows\System32\wintrust.dll BaseAddress: 0x7ffa326a0000 Size: 0x6b000 Endaddress: 0x7ffa3270b000
Module name: C:\Windows\System32\kerberos.dll BaseAddress: 0x7ffa314d0000 Size: 0x126000 Endaddress: 0x7ffa315f6000
Module name: C:\Windows\System32\userenv.dll BaseAddress: 0x7ffa314a0000 Size: 0x28000 Endaddress: 0x7ffa314c8000
Module name: C:\Windows\System32\KerbClientShared.dll BaseAddress: 0x7ffa31460000 Size: 0x3a000 Endaddress: 0x7ffa3149a000
Module name: C:\Windows\System32\ws2_32.dll BaseAddress: 0x7ffa33fb0000 Size: 0x71000 Endaddress: 0x7ffa34021000
Module name: C:\Windows\System32\gpapi.dll BaseAddress: 0x7ffa31430000 Size: 0x26000 Endaddress: 0x7ffa31456000
Module name: C:\Windows\System32\cryptdll.dll BaseAddress: 0x7ffa31410000 Size: 0x15000 Endaddress: 0x7ffa31425000
Module name: C:\Windows\System32\mswsock.dll BaseAddress: 0x7ffa313a0000 Size: 0x69000 Endaddress: 0x7ffa31409000
Module name: C:\Windows\System32\msv1_0.dll BaseAddress: 0x7ffa31310000 Size: 0x89000 Endaddress: 0x7ffa31399000
Module name: C:\Windows\System32\NtlmShared.dll BaseAddress: 0x7ffa31300000 Size: 0xe000 Endaddress: 0x7ffa3130e000
Module name: C:\Windows\System32\netlogon.dll BaseAddress: 0x7ffa31220000 Size: 0xdc000 Endaddress: 0x7ffa312fc000
Module name: C:\Windows\System32\gmsaclient.dll BaseAddress: 0x7ffa31210000 Size: 0xf000 Endaddress: 0x7ffa3121f000
Module name: C:\Windows\System32\TSpkg.dll BaseAddress: 0x7ffa311e0000 Size: 0x2c000 Endaddress: 0x7ffa3120c000
Module name: C:\Windows\System32\sspicli.dll BaseAddress: 0x7ffa31190000 Size: 0x43000 Endaddress: 0x7ffa311d3000
Module name: C:\Windows\System32\pku2u.dll BaseAddress: 0x7ffa31130000 Size: 0x5c000 Endaddress: 0x7ffa3118c000
Module name: C:\Windows\System32\cloudAP.dll BaseAddress: 0x7ffa31080000 Size: 0xa4000 Endaddress: 0x7ffa31124000
Module name: C:\Windows\System32\profapi.dll BaseAddress: 0x7ffa31e30000 Size: 0x21000 Endaddress: 0x7ffa31e51000
Module name: C:\Windows\System32\aadcloudap.dll BaseAddress: 0x7ffa30f90000 Size: 0xe4000 Endaddress: 0x7ffa31074000
Module name: C:\Windows\System32\ntmarta.dll BaseAddress: 0x7ffa30f50000 Size: 0x34000 Endaddress: 0x7ffa30f84000
Module name: C:\Windows\System32\kernel.appcore.dll BaseAddress: 0x7ffa30f30000 Size: 0x18000 Endaddress: 0x7ffa30f48000
Module name: C:\Windows\System32\MicrosoftAccountCloudAP.dll BaseAddress: 0x7ffa30ed0000 Size: 0x55000 Endaddress: 0x7ffa30f25000
Module name: C:\Windows\System32\dpapi.dll BaseAddress: 0x7ffa31b60000 Size: 0xa000 Endaddress: 0x7ffa31b6a000
Module name: C:\Windows\System32\rsaenh.dll BaseAddress: 0x7ffa30e90000 Size: 0x35000 Endaddress: 0x7ffa30ec5000
Module name: C:\Windows\System32\wdigest.dll BaseAddress: 0x7ffa30e40000 Size: 0x48000 Endaddress: 0x7ffa30e88000
Module name: C:\Windows\System32\schannel.dll BaseAddress: 0x7ffa30d90000 Size: 0xa7000 Endaddress: 0x7ffa30e37000
Module name: C:\Windows\System32\SFAPM.dll BaseAddress: 0x7ffa30d30000 Size: 0x52000 Endaddress: 0x7ffa30d82000
Module name: C:\Windows\System32\shlwapi.dll BaseAddress: 0x7ffa33700000 Size: 0x5e000 Endaddress: 0x7ffa3375e000
Module name: C:\Windows\System32\shell32.dll BaseAddress: 0x7ffa32910000 Size: 0x85f000 Endaddress: 0x7ffa3316f000
Module name: C:\Windows\System32\WTDSENSOR.dll BaseAddress: 0x7ffa30d20000 Size: 0xa000 Endaddress: 0x7ffa30d2a000
Module name: C:\Windows\System32\secur32.dll BaseAddress: 0x7ffa30d10000 Size: 0xc000 Endaddress: 0x7ffa30d1c000
Module name: C:\Windows\System32\user32.dll BaseAddress: 0x7ffa338c0000 Size: 0x1ae000 Endaddress: 0x7ffa33a6e000
Module name: C:\Windows\System32\win32u.dll BaseAddress: 0x7ffa32740000 Size: 0x26000 Endaddress: 0x7ffa32766000
Module name: C:\Windows\System32\gdi32.dll BaseAddress: 0x7ffa33400000 Size: 0x29000 Endaddress: 0x7ffa33429000
Module name: C:\Windows\System32\gdi32full.dll BaseAddress: 0x7ffa32770000 Size: 0x119000 Endaddress: 0x7ffa32889000
Module name: C:\Windows\System32\ole32.dll BaseAddress: 0x7ffa33550000 Size: 0x1a5000 Endaddress: 0x7ffa336f5000
Module name: C:\Windows\System32\powrprof.dll BaseAddress: 0x7ffa31dc0000 Size: 0x4d000 Endaddress: 0x7ffa31e0d000
Module name: C:\Windows\System32\wtsapi32.dll BaseAddress: 0x7ffa30cf0000 Size: 0x14000 Endaddress: 0x7ffa30d04000
Module name: C:\Windows\System32\umpdc.dll BaseAddress: 0x7ffa31da0000 Size: 0x13000 Endaddress: 0x7ffa31db3000
Module name: C:\Windows\System32\dpapisrv.dll BaseAddress: 0x7ffa30ca0000 Size: 0x4d000 Endaddress: 0x7ffa30ced000
Module name: C:\Windows\System32\sspisrv.dll BaseAddress: 0x7ffa30c90000 Size: 0xc000 Endaddress: 0x7ffa30c9c000
Module name: C:\Windows\System32\kdcpw.dll BaseAddress: 0x7ffa30b70000 Size: 0x14000 Endaddress: 0x7ffa30b84000
Module name: C:\Windows\System32\scecli.dll BaseAddress: 0x7ffa30ba0000 Size: 0x5a000 Endaddress: 0x7ffa30bfa000
Module name: C:\Windows\System32\dnsapi.dll BaseAddress: 0x7ffa30a20000 Size: 0xf8000 Endaddress: 0x7ffa30b18000
Module name: C:\Windows\System32\IPHLPAPI.DLL BaseAddress: 0x7ffa309b0000 Size: 0x2d000 Endaddress: 0x7ffa309dd000
Module name: C:\Windows\System32\nsi.dll BaseAddress: 0x7ffa33fa0000 Size: 0x9000 Endaddress: 0x7ffa33fa9000
Module name: C:\Windows\System32\netutils.dll BaseAddress: 0x7ffa309a0000 Size: 0xc000 Endaddress: 0x7ffa309ac000
Module name: C:\Windows\System32\winsta.dll BaseAddress: 0x7ffa31b70000 Size: 0x66000 Endaddress: 0x7ffa31bd6000
Module name: C:\Windows\System32\keyiso.dll BaseAddress: 0x7ffa1e8e0000 Size: 0x1d000 Endaddress: 0x7ffa1e8fd000
Module name: C:\Windows\System32\NCRYPTPROV.DLL BaseAddress: 0x7ffa1f900000 Size: 0x6a000 Endaddress: 0x7ffa1f96a000
Module name: C:\Windows\System32\vaultsvc.dll BaseAddress: 0x7ffa1de20000 Size: 0x61000 Endaddress: 0x7ffa1de81000
Module name: C:\Windows\System32\ncryptsslp.dll BaseAddress: 0x7ffa1da90000 Size: 0x27000 Endaddress: 0x7ffa1dab7000
Module name: C:\Windows\System32\dssenh.dll BaseAddress: 0x7ffa1cd80000 Size: 0x29000 Endaddress: 0x7ffa1cda9000
Module name: C:\Windows\System32\wevtapi.dll BaseAddress: 0x7ffa29540000 Size: 0x54000 Endaddress: 0x7ffa29594000
Module name: C:\Windows\System32\SecureTimeAggregator.dll BaseAddress: 0x7ffa1c2d0000 Size: 0x22000 Endaddress: 0x7ffa1c2f2000
Module name: C:\Windows\System32\cryptnet.dll BaseAddress: 0x7ffa1c290000 Size: 0x32000 Endaddress: 0x7ffa1c2c2000
Module name: C:\Windows\System32\authz.dll BaseAddress: 0x7ffa30b20000 Size: 0x4e000 Endaddress: 0x7ffa30b6e000
Module name: C:\Windows\System32\clbcatq.dll BaseAddress: 0x7ffa33ef0000 Size: 0xb0000 Endaddress: 0x7ffa33fa0000
Module name: C:\Windows\System32\certpoleng.dll BaseAddress: 0x7ff9dd4e0000 Size: 0x31000 Endaddress: 0x7ff9dd511000
Module name: C:\Windows\System32\wkscli.dll BaseAddress: 0x7ffa293b0000 Size: 0x1a000 Endaddress: 0x7ffa293ca000
VA Start: 0x7ffe0000, RVA: 0x334bd, Size: 0x1000
VA Start: 0x7ffe6000, RVA: 0x344bd, Size: 0x1000
VA Start: 0xb2ca59d000, RVA: 0x354bd, Size: 0x1000
VA Start: 0xb2ca5a2000, RVA: 0x364bd, Size: 0x2000
VA Start: 0xb2ca5a8000, RVA: 0x384bd, Size: 0x4000
VA Start: 0xb2ca5ae000, RVA: 0x3c4bd, Size: 0x2000
VA Start: 0xb2ca5b2000, RVA: 0x3e4bd, Size: 0x2000
VA Start: 0xb2ca5bc000, RVA: 0x404bd, Size: 0x6000
VA Start: 0xb2ca5cc000, RVA: 0x464bd, Size: 0x2000
VA Start: 0xb2ca5d2000, RVA: 0x484bd, Size: 0x2000
VA Start: 0xb2ca5d8000, RVA: 0x4a4bd, Size: 0x2000
VA Start: 0xb2ca674000, RVA: 0x4c4bd, Size: 0xc000
VA Start: 0xb2ca774000, RVA: 0x584bd, Size: 0xc000
VA Start: 0xb2ca874000, RVA: 0x644bd, Size: 0xc000
VA Start: 0xb2ca8f4000, RVA: 0x704bd, Size: 0xc000
VA Start: 0xb2ca974000, RVA: 0x7c4bd, Size: 0xc000
VA Start: 0xb2ca9f4000, RVA: 0x884bd, Size: 0xc000
VA Start: 0xb2caa74000, RVA: 0x944bd, Size: 0xc000
VA Start: 0xb2caaf4000, RVA: 0xa04bd, Size: 0xc000
VA Start: 0xb2cab74000, RVA: 0xac4bd, Size: 0xc000
VA Start: 0xb2cabf4000, RVA: 0xb84bd, Size: 0xc000
VA Start: 0xb2cacf4000, RVA: 0xc44bd, Size: 0xc000
VA Start: 0x1dcaec40000, RVA: 0xd04bd, Size: 0x10000
VA Start: 0x1dcaec50000, RVA: 0xe04bd, Size: 0x3000
VA Start: 0x1dcaec60000, RVA: 0xe34bd, Size: 0x1f000
VA Start: 0x1dcaec80000, RVA: 0x1024bd, Size: 0x4000
VA Start: 0x1dcaec90000, RVA: 0x1064bd, Size: 0x1000
VA Start: 0x1dcaeca0000, RVA: 0x1074bd, Size: 0x2000
VA Start: 0x1dcaecb0000, RVA: 0x1094bd, Size: 0x11000
VA Start: 0x1dcaecd0000, RVA: 0x11a4bd, Size: 0x11000
VA Start: 0x1dcaecf0000, RVA: 0x12b4bd, Size: 0x3000
VA Start: 0x1dcaed00000, RVA: 0x12e4bd, Size: 0x5000
VA Start: 0x1dcaed10000, RVA: 0x1334bd, Size: 0xce000
VA Start: 0x1dcaede0000, RVA: 0x2014bd, Size: 0x11000
VA Start: 0x1dcaee00000, RVA: 0x2124bd, Size: 0x12000
VA Start: 0x1dcaee13000, RVA: 0x2244bd, Size: 0x19000
VA Start: 0x1dcaee2d000, RVA: 0x23d4bd, Size: 0x26000
VA Start: 0x1dcaee54000, RVA: 0x2634bd, Size: 0x24000
VA Start: 0x1dcaee79000, RVA: 0x2874bd, Size: 0x16000
VA Start: 0x1dcaee90000, RVA: 0x29d4bd, Size: 0x20000
VA Start: 0x1dcaeeb1000, RVA: 0x2bd4bd, Size: 0x5b000
VA Start: 0x1dcaef13000, RVA: 0x3184bd, Size: 0x1000
VA Start: 0x1dcaf000000, RVA: 0x3194bd, Size: 0x11000
VA Start: 0x1dcaf020000, RVA: 0x32a4bd, Size: 0x2000
VA Start: 0x1dcaf030000, RVA: 0x32c4bd, Size: 0x2000
VA Start: 0x1dcaf040000, RVA: 0x32e4bd, Size: 0x1000
VA Start: 0x1dcaf050000, RVA: 0x32f4bd, Size: 0x1000
VA Start: 0x1dcaf060000, RVA: 0x3304bd, Size: 0x1000
VA Start: 0x1dcaf070000, RVA: 0x3314bd, Size: 0x33a000
VA Start: 0x1dcaf3b0000, RVA: 0x66b4bd, Size: 0x1000
VA Start: 0x1dcaf3c0000, RVA: 0x66c4bd, Size: 0x10000
VA Start: 0x1dcaf3d0000, RVA: 0x67c4bd, Size: 0x3000
VA Start: 0x1dcaf3e0000, RVA: 0x67f4bd, Size: 0x1000
VA Start: 0x1dcaf3f0000, RVA: 0x6804bd, Size: 0x11000
VA Start: 0x1dcaf410000, RVA: 0x6914bd, Size: 0x1000
VA Start: 0x1dcaf610000, RVA: 0x6924bd, Size: 0x4000
VA Start: 0x1dcaf620000, RVA: 0x6964bd, Size: 0x181000
VA Start: 0x1dcaf7b0000, RVA: 0x8174bd, Size: 0x8000
VA Start: 0x1dcaf880000, RVA: 0x81f4bd, Size: 0x1000
VA Start: 0x1dcaf890000, RVA: 0x8204bd, Size: 0x1000
VA Start: 0x1dcaf8a0000, RVA: 0x8214bd, Size: 0x1000
VA Start: 0x1dcaf8b0000, RVA: 0x8224bd, Size: 0x1000
VA Start: 0x1dcaf8c0000, RVA: 0x8234bd, Size: 0x1000
VA Start: 0x1dcaf8d0000, RVA: 0x8244bd, Size: 0x1000
VA Start: 0x1dcaf8e0000, RVA: 0x8254bd, Size: 0x1000
VA Start: 0x1dcaf8f0000, RVA: 0x8264bd, Size: 0x1000
VA Start: 0x1dcaf900000, RVA: 0x8274bd, Size: 0x1000
VA Start: 0x1dcaf910000, RVA: 0x8284bd, Size: 0x1000
VA Start: 0x1dcaf920000, RVA: 0x8294bd, Size: 0x1000
VA Start: 0x1dcaf940000, RVA: 0x82a4bd, Size: 0xa000
VA Start: 0x1dcaf950000, RVA: 0x8344bd, Size: 0x1000
VA Start: 0x1dcaf960000, RVA: 0x8354bd, Size: 0x1000
VA Start: 0x1dcaf970000, RVA: 0x8364bd, Size: 0x7000
VA Start: 0x1dcaf980000, RVA: 0x83d4bd, Size: 0x1000
VA Start: 0x1dcaf990000, RVA: 0x83e4bd, Size: 0x48000
VA Start: 0x1dcafa00000, RVA: 0x8864bd, Size: 0x1a000
VA Start: 0x1dcafa23000, RVA: 0x8a04bd, Size: 0x2e000
VA Start: 0x1dcafa52000, RVA: 0x8ce4bd, Size: 0x2c000
VA Start: 0x1dcafa7f000, RVA: 0x8fa4bd, Size: 0x93000
VA Start: 0x1dcafb13000, RVA: 0x98d4bd, Size: 0x90000
VA Start: 0x1dcafba4000, RVA: 0xa1d4bd, Size: 0x1c000
VA Start: 0x1dcafbc1000, RVA: 0xa394bd, Size: 0x3f000
VA Start: 0x1dcafc00000, RVA: 0xa784bd, Size: 0x1a000
VA Start: 0x1dcafc1b000, RVA: 0xa924bd, Size: 0x2b000
VA Start: 0x1dcafc64000, RVA: 0xabd4bd, Size: 0x14000
VA Start: 0x1dcafc7c000, RVA: 0xad14bd, Size: 0xe000
VA Start: 0x1dcafc93000, RVA: 0xadf4bd, Size: 0xd000
VA Start: 0x1dcafca1000, RVA: 0xaec4bd, Size: 0xe000
VA Start: 0x1dcafcb2000, RVA: 0xafa4bd, Size: 0x2000
VA Start: 0x1dcafcb5000, RVA: 0xafc4bd, Size: 0x3000
VA Start: 0x1dcafcba000, RVA: 0xaff4bd, Size: 0x1000
VA Start: 0x7df452bf0000, RVA: 0xb004bd, Size: 0x5000
VA Start: 0x7df456885000, RVA: 0xb054bd, Size: 0x1000
VA Start: 0x7df552cf0000, RVA: 0xb064bd, Size: 0x1000
VA Start: 0x7df552d87000, RVA: 0xb074bd, Size: 0x1000
VA Start: 0x7df554d10000, RVA: 0xb084bd, Size: 0x1000
VA Start: 0x7df554d20000, RVA: 0xb094bd, Size: 0x1000
VA Start: 0x7dfcc78ff000, RVA: 0xb0a4bd, Size: 0x1000
VA Start: 0x7ff52d413000, RVA: 0xb0b4bd, Size: 0x2000
VA Start: 0x7ff53c483000, RVA: 0xb0d4bd, Size: 0x2000
VA Start: 0x7ff53d43a000, RVA: 0xb0f4bd, Size: 0x2000
VA Start: 0x7ff53d466000, RVA: 0xb114bd, Size: 0x1000
VA Start: 0x7ff53d49a000, RVA: 0xb124bd, Size: 0x1000
VA Start: 0x7ff53d4a8000, RVA: 0xb134bd, Size: 0x3000
VA Start: 0x7ff53d4d3000, RVA: 0xb164bd, Size: 0x1000
VA Start: 0x7ff53d514000, RVA: 0xb174bd, Size: 0x2000
VA Start: 0x7ff53d57a000, RVA: 0xb194bd, Size: 0x3000
VA Start: 0x7ff53d77e000, RVA: 0xb1c4bd, Size: 0x2000
VA Start: 0x7ff53d785000, RVA: 0xb1e4bd, Size: 0x2000
VA Start: 0x7ff53d956000, RVA: 0xb204bd, Size: 0xa000
VA Start: 0x7ff53d962000, RVA: 0xb2a4bd, Size: 0x39000
VA Start: 0x7ff53d99d000, RVA: 0xb634bd, Size: 0x3000
VA Start: 0x7ff53d9a6000, RVA: 0xb664bd, Size: 0x4000
VA Start: 0x7ff53d9af000, RVA: 0xb6a4bd, Size: 0x47000
VA Start: 0x7ff53da00000, RVA: 0xbb14bd, Size: 0xe000
VA Start: 0x7ff53da13000, RVA: 0xbbf4bd, Size: 0x7000
VA Start: 0x7ff53da2b000, RVA: 0xbc64bd, Size: 0x6000
VA Start: 0x7ff53da35000, RVA: 0xbcc4bd, Size: 0x3000
VA Start: 0x7ff53da3e000, RVA: 0xbcf4bd, Size: 0x8000
VA Start: 0x7ff53da48000, RVA: 0xbd74bd, Size: 0x15000
VA Start: 0x7ff53da5f000, RVA: 0xbec4bd, Size: 0x9000
VA Start: 0x7ff61b8f0000, RVA: 0xbf54bd, Size: 0x1000
VA Start: 0x7ff61b8f1000, RVA: 0xbf64bd, Size: 0x6000
VA Start: 0x7ff61b8f7000, RVA: 0xbfc4bd, Size: 0x6000
VA Start: 0x7ff61b8fd000, RVA: 0xc024bd, Size: 0x1000
VA Start: 0x7ff61b8fe000, RVA: 0xc034bd, Size: 0x4000
VA Start: 0x7ff9dd4e0000, RVA: 0xc074bd, Size: 0x1000
VA Start: 0x7ff9dd4e1000, RVA: 0xc084bd, Size: 0x1b000
VA Start: 0x7ff9dd4fc000, RVA: 0xc234bd, Size: 0xc000
VA Start: 0x7ff9dd508000, RVA: 0xc2f4bd, Size: 0x2000
VA Start: 0x7ff9dd50a000, RVA: 0xc314bd, Size: 0x7000
VA Start: 0x7ffa1c290000, RVA: 0xc384bd, Size: 0x1000
VA Start: 0x7ffa1c291000, RVA: 0xc394bd, Size: 0x22000
VA Start: 0x7ffa1c2b3000, RVA: 0xc5b4bd, Size: 0x9000
VA Start: 0x7ffa1c2bc000, RVA: 0xc644bd, Size: 0x1000
VA Start: 0x7ffa1c2bd000, RVA: 0xc654bd, Size: 0x5000
VA Start: 0x7ffa1c2d0000, RVA: 0xc6a4bd, Size: 0x1000
VA Start: 0x7ffa1c2d1000, RVA: 0xc6b4bd, Size: 0xc000
VA Start: 0x7ffa1c2dd000, RVA: 0xc774bd, Size: 0x8000
VA Start: 0x7ffa1c2e5000, RVA: 0xc7f4bd, Size: 0x9000
VA Start: 0x7ffa1c2ee000, RVA: 0xc884bd, Size: 0x4000
VA Start: 0x7ffa1cd80000, RVA: 0xc8c4bd, Size: 0x1000
VA Start: 0x7ffa1cd81000, RVA: 0xc8d4bd, Size: 0x18000
VA Start: 0x7ffa1cd99000, RVA: 0xca54bd, Size: 0x7000
VA Start: 0x7ffa1cda0000, RVA: 0xcac4bd, Size: 0x1000
VA Start: 0x7ffa1cda1000, RVA: 0xcad4bd, Size: 0x8000
VA Start: 0x7ffa1da90000, RVA: 0xcb54bd, Size: 0x1000
VA Start: 0x7ffa1da91000, RVA: 0xcb64bd, Size: 0x15000
VA Start: 0x7ffa1daa6000, RVA: 0xccb4bd, Size: 0x7000
VA Start: 0x7ffa1daad000, RVA: 0xcd24bd, Size: 0x1000
VA Start: 0x7ffa1daae000, RVA: 0xcd34bd, Size: 0x3000
VA Start: 0x7ffa1dab1000, RVA: 0xcd64bd, Size: 0x2000
VA Start: 0x7ffa1dab3000, RVA: 0xcd84bd, Size: 0x4000
VA Start: 0x7ffa1de20000, RVA: 0xcdc4bd, Size: 0x1000
VA Start: 0x7ffa1de21000, RVA: 0xcdd4bd, Size: 0x48000
VA Start: 0x7ffa1de69000, RVA: 0xd254bd, Size: 0x10000
VA Start: 0x7ffa1de79000, RVA: 0xd354bd, Size: 0x2000
VA Start: 0x7ffa1de7b000, RVA: 0xd374bd, Size: 0x6000
VA Start: 0x7ffa1e8e0000, RVA: 0xd3d4bd, Size: 0x1000
VA Start: 0x7ffa1e8e1000, RVA: 0xd3e4bd, Size: 0xf000
VA Start: 0x7ffa1e8f0000, RVA: 0xd4d4bd, Size: 0x9000
VA Start: 0x7ffa1e8f9000, RVA: 0xd564bd, Size: 0x1000
VA Start: 0x7ffa1e8fa000, RVA: 0xd574bd, Size: 0x3000
VA Start: 0x7ffa1f900000, RVA: 0xd5a4bd, Size: 0x1000
VA Start: 0x7ffa1f901000, RVA: 0xd5b4bd, Size: 0x50000
VA Start: 0x7ffa1f951000, RVA: 0xdab4bd, Size: 0x11000
VA Start: 0x7ffa1f962000, RVA: 0xdbc4bd, Size: 0x2000
VA Start: 0x7ffa1f964000, RVA: 0xdbe4bd, Size: 0x6000
VA Start: 0x7ffa293b0000, RVA: 0xdc44bd, Size: 0x1000
VA Start: 0x7ffa293b1000, RVA: 0xdc54bd, Size: 0xc000
VA Start: 0x7ffa293bd000, RVA: 0xdd14bd, Size: 0x8000
VA Start: 0x7ffa293c5000, RVA: 0xdd94bd, Size: 0x1000
VA Start: 0x7ffa293c6000, RVA: 0xdda4bd, Size: 0x4000
VA Start: 0x7ffa29540000, RVA: 0xdde4bd, Size: 0x1000
VA Start: 0x7ffa29541000, RVA: 0xddf4bd, Size: 0x3c000
VA Start: 0x7ffa2957d000, RVA: 0xe1b4bd, Size: 0xf000
VA Start: 0x7ffa2958c000, RVA: 0xe2a4bd, Size: 0x1000
VA Start: 0x7ffa2958d000, RVA: 0xe2b4bd, Size: 0x7000
VA Start: 0x7ffa309a0000, RVA: 0xe324bd, Size: 0x1000
VA Start: 0x7ffa309a1000, RVA: 0xe334bd, Size: 0x5000
VA Start: 0x7ffa309a6000, RVA: 0xe384bd, Size: 0x2000
VA Start: 0x7ffa309a8000, RVA: 0xe3a4bd, Size: 0x1000
VA Start: 0x7ffa309a9000, RVA: 0xe3b4bd, Size: 0x3000
VA Start: 0x7ffa309b0000, RVA: 0xe3e4bd, Size: 0x1000
VA Start: 0x7ffa309b1000, RVA: 0xe3f4bd, Size: 0x1e000
VA Start: 0x7ffa309cf000, RVA: 0xe5d4bd, Size: 0x8000
VA Start: 0x7ffa309d7000, RVA: 0xe654bd, Size: 0x1000
VA Start: 0x7ffa309d8000, RVA: 0xe664bd, Size: 0x5000
VA Start: 0x7ffa30a20000, RVA: 0xe6b4bd, Size: 0x1000
VA Start: 0x7ffa30a21000, RVA: 0xe6c4bd, Size: 0xb3000
VA Start: 0x7ffa30ad4000, RVA: 0xf1f4bd, Size: 0x26000
VA Start: 0x7ffa30afa000, RVA: 0xf454bd, Size: 0x2000
VA Start: 0x7ffa30afc000, RVA: 0xf474bd, Size: 0x1c000
VA Start: 0x7ffa30b20000, RVA: 0xf634bd, Size: 0x1000
VA Start: 0x7ffa30b21000, RVA: 0xf644bd, Size: 0x2c000
VA Start: 0x7ffa30b4d000, RVA: 0xf904bd, Size: 0x1a000
VA Start: 0x7ffa30b67000, RVA: 0xfaa4bd, Size: 0x1000
VA Start: 0x7ffa30b68000, RVA: 0xfab4bd, Size: 0x6000
VA Start: 0x7ffa30b70000, RVA: 0xfb14bd, Size: 0x1000
VA Start: 0x7ffa30b71000, RVA: 0xfb24bd, Size: 0xb000
VA Start: 0x7ffa30b7c000, RVA: 0xfbd4bd, Size: 0x3000
VA Start: 0x7ffa30b7f000, RVA: 0xfc04bd, Size: 0x1000
VA Start: 0x7ffa30b80000, RVA: 0xfc14bd, Size: 0x4000
VA Start: 0x7ffa30ba0000, RVA: 0xfc54bd, Size: 0x1000
VA Start: 0x7ffa30ba1000, RVA: 0xfc64bd, Size: 0x38000
VA Start: 0x7ffa30bd9000, RVA: 0xffe4bd, Size: 0x18000
VA Start: 0x7ffa30bf1000, RVA: 0x10164bd, Size: 0x3000
VA Start: 0x7ffa30bf4000, RVA: 0x10194bd, Size: 0x6000
VA Start: 0x7ffa30c90000, RVA: 0x101f4bd, Size: 0x1000
VA Start: 0x7ffa30c91000, RVA: 0x10204bd, Size: 0x3000
VA Start: 0x7ffa30c94000, RVA: 0x10234bd, Size: 0x4000
VA Start: 0x7ffa30c98000, RVA: 0x10274bd, Size: 0x1000
VA Start: 0x7ffa30c99000, RVA: 0x10284bd, Size: 0x3000
VA Start: 0x7ffa30ca0000, RVA: 0x102b4bd, Size: 0x1000
VA Start: 0x7ffa30ca1000, RVA: 0x102c4bd, Size: 0x34000
VA Start: 0x7ffa30cd5000, RVA: 0x10604bd, Size: 0xd000
VA Start: 0x7ffa30ce2000, RVA: 0x106d4bd, Size: 0x2000
VA Start: 0x7ffa30ce4000, RVA: 0x106f4bd, Size: 0x9000
VA Start: 0x7ffa30cf0000, RVA: 0x10784bd, Size: 0x1000
VA Start: 0x7ffa30cf1000, RVA: 0x10794bd, Size: 0xa000
VA Start: 0x7ffa30cfb000, RVA: 0x10834bd, Size: 0x4000
VA Start: 0x7ffa30cff000, RVA: 0x10874bd, Size: 0x1000
VA Start: 0x7ffa30d00000, RVA: 0x10884bd, Size: 0x4000
VA Start: 0x7ffa30d10000, RVA: 0x108c4bd, Size: 0x1000
VA Start: 0x7ffa30d11000, RVA: 0x108d4bd, Size: 0x3000
VA Start: 0x7ffa30d14000, RVA: 0x10904bd, Size: 0x3000
VA Start: 0x7ffa30d17000, RVA: 0x10934bd, Size: 0x1000
VA Start: 0x7ffa30d18000, RVA: 0x10944bd, Size: 0x4000
VA Start: 0x7ffa30d20000, RVA: 0x10984bd, Size: 0x1000
VA Start: 0x7ffa30d21000, RVA: 0x10994bd, Size: 0x3000
VA Start: 0x7ffa30d24000, RVA: 0x109c4bd, Size: 0x2000
VA Start: 0x7ffa30d26000, RVA: 0x109e4bd, Size: 0x1000
VA Start: 0x7ffa30d27000, RVA: 0x109f4bd, Size: 0x3000
VA Start: 0x7ffa30d30000, RVA: 0x10a24bd, Size: 0x1000
VA Start: 0x7ffa30d31000, RVA: 0x10a34bd, Size: 0x2b000
VA Start: 0x7ffa30d5c000, RVA: 0x10ce4bd, Size: 0xe000
VA Start: 0x7ffa30d6a000, RVA: 0x10dc4bd, Size: 0x3000
VA Start: 0x7ffa30d6d000, RVA: 0x10df4bd, Size: 0xf000
VA Start: 0x7ffa30d7c000, RVA: 0x10ee4bd, Size: 0x1000
VA Start: 0x7ffa30d7d000, RVA: 0x10ef4bd, Size: 0x5000
VA Start: 0x7ffa30d90000, RVA: 0x10f44bd, Size: 0x1000
VA Start: 0x7ffa30d91000, RVA: 0x10f54bd, Size: 0x84000
VA Start: 0x7ffa30e15000, RVA: 0x11794bd, Size: 0x15000
VA Start: 0x7ffa30e2a000, RVA: 0x118e4bd, Size: 0x3000
VA Start: 0x7ffa30e2d000, RVA: 0x11914bd, Size: 0xa000
VA Start: 0x7ffa30e40000, RVA: 0x119b4bd, Size: 0x1000
VA Start: 0x7ffa30e41000, RVA: 0x119c4bd, Size: 0x36000
VA Start: 0x7ffa30e77000, RVA: 0x11d24bd, Size: 0xa000
VA Start: 0x7ffa30e81000, RVA: 0x11dc4bd, Size: 0x2000
VA Start: 0x7ffa30e83000, RVA: 0x11de4bd, Size: 0x5000
VA Start: 0x7ffa30e90000, RVA: 0x11e34bd, Size: 0x1000
VA Start: 0x7ffa30e91000, RVA: 0x11e44bd, Size: 0x24000
VA Start: 0x7ffa30eb5000, RVA: 0x12084bd, Size: 0x8000
VA Start: 0x7ffa30ebd000, RVA: 0x12104bd, Size: 0x1000
VA Start: 0x7ffa30ebe000, RVA: 0x12114bd, Size: 0x7000
VA Start: 0x7ffa30ed0000, RVA: 0x12184bd, Size: 0x1000
VA Start: 0x7ffa30ed1000, RVA: 0x12194bd, Size: 0x32000
VA Start: 0x7ffa30f03000, RVA: 0x124b4bd, Size: 0x1a000
VA Start: 0x7ffa30f1d000, RVA: 0x12654bd, Size: 0x2000
VA Start: 0x7ffa30f1f000, RVA: 0x12674bd, Size: 0x6000
VA Start: 0x7ffa30f30000, RVA: 0x126d4bd, Size: 0x1000
VA Start: 0x7ffa30f31000, RVA: 0x126e4bd, Size: 0x9000
VA Start: 0x7ffa30f3a000, RVA: 0x12774bd, Size: 0x9000
VA Start: 0x7ffa30f43000, RVA: 0x12804bd, Size: 0x1000
VA Start: 0x7ffa30f44000, RVA: 0x12814bd, Size: 0x4000
VA Start: 0x7ffa30f50000, RVA: 0x12854bd, Size: 0x1000
VA Start: 0x7ffa30f51000, RVA: 0x12864bd, Size: 0x24000
VA Start: 0x7ffa30f75000, RVA: 0x12aa4bd, Size: 0x8000
VA Start: 0x7ffa30f7d000, RVA: 0x12b24bd, Size: 0x2000
VA Start: 0x7ffa30f7f000, RVA: 0x12b44bd, Size: 0x5000
VA Start: 0x7ffa30f90000, RVA: 0x12b94bd, Size: 0x1000
VA Start: 0x7ffa30f91000, RVA: 0x12ba4bd, Size: 0x9a000
VA Start: 0x7ffa3102b000, RVA: 0x13544bd, Size: 0x37000
VA Start: 0x7ffa31062000, RVA: 0x138b4bd, Size: 0x2000
VA Start: 0x7ffa31064000, RVA: 0x138d4bd, Size: 0x10000
VA Start: 0x7ffa31080000, RVA: 0x139d4bd, Size: 0x1000
VA Start: 0x7ffa31081000, RVA: 0x139e4bd, Size: 0x82000
VA Start: 0x7ffa31103000, RVA: 0x14204bd, Size: 0x17000
VA Start: 0x7ffa3111a000, RVA: 0x14374bd, Size: 0x2000
VA Start: 0x7ffa3111c000, RVA: 0x14394bd, Size: 0x8000
VA Start: 0x7ffa31130000, RVA: 0x14414bd, Size: 0x1000
VA Start: 0x7ffa31131000, RVA: 0x14424bd, Size: 0x43000
VA Start: 0x7ffa31174000, RVA: 0x14854bd, Size: 0xb000
VA Start: 0x7ffa3117f000, RVA: 0x14904bd, Size: 0x2000
VA Start: 0x7ffa31181000, RVA: 0x14924bd, Size: 0x5000
VA Start: 0x7ffa31186000, RVA: 0x14974bd, Size: 0x6000
VA Start: 0x7ffa31190000, RVA: 0x149d4bd, Size: 0x1000
VA Start: 0x7ffa31191000, RVA: 0x149e4bd, Size: 0x1f000
VA Start: 0x7ffa311b0000, RVA: 0x14bd4bd, Size: 0x1b000
VA Start: 0x7ffa311cb000, RVA: 0x14d84bd, Size: 0x2000
VA Start: 0x7ffa311cd000, RVA: 0x14da4bd, Size: 0x6000
VA Start: 0x7ffa311e0000, RVA: 0x14e04bd, Size: 0x1000
VA Start: 0x7ffa311e1000, RVA: 0x14e14bd, Size: 0x1d000
VA Start: 0x7ffa311fe000, RVA: 0x14fe4bd, Size: 0x7000
VA Start: 0x7ffa31205000, RVA: 0x15054bd, Size: 0x2000
VA Start: 0x7ffa31207000, RVA: 0x15074bd, Size: 0x5000
VA Start: 0x7ffa31210000, RVA: 0x150c4bd, Size: 0x1000
VA Start: 0x7ffa31211000, RVA: 0x150d4bd, Size: 0x7000
VA Start: 0x7ffa31218000, RVA: 0x15144bd, Size: 0x2000
VA Start: 0x7ffa3121a000, RVA: 0x15164bd, Size: 0x1000
VA Start: 0x7ffa3121b000, RVA: 0x15174bd, Size: 0x4000
VA Start: 0x7ffa31220000, RVA: 0x151b4bd, Size: 0x1000
VA Start: 0x7ffa31221000, RVA: 0x151c4bd, Size: 0x72000
VA Start: 0x7ffa31293000, RVA: 0x158e4bd, Size: 0x5d000
VA Start: 0x7ffa312f0000, RVA: 0x15eb4bd, Size: 0x4000
VA Start: 0x7ffa312f4000, RVA: 0x15ef4bd, Size: 0x1000
VA Start: 0x7ffa312f5000, RVA: 0x15f04bd, Size: 0x7000
VA Start: 0x7ffa31300000, RVA: 0x15f74bd, Size: 0x1000
VA Start: 0x7ffa31301000, RVA: 0x15f84bd, Size: 0x5000
VA Start: 0x7ffa31306000, RVA: 0x15fd4bd, Size: 0x3000
VA Start: 0x7ffa31309000, RVA: 0x16004bd, Size: 0x1000
VA Start: 0x7ffa3130a000, RVA: 0x16014bd, Size: 0x4000
VA Start: 0x7ffa31310000, RVA: 0x16054bd, Size: 0x1000
VA Start: 0x7ffa31311000, RVA: 0x16064bd, Size: 0x68000
VA Start: 0x7ffa31379000, RVA: 0x166e4bd, Size: 0x13000
VA Start: 0x7ffa3138c000, RVA: 0x16814bd, Size: 0x5000
VA Start: 0x7ffa31391000, RVA: 0x16864bd, Size: 0x8000
VA Start: 0x7ffa313a0000, RVA: 0x168e4bd, Size: 0x1000
VA Start: 0x7ffa313a1000, RVA: 0x168f4bd, Size: 0x51000
VA Start: 0x7ffa313f2000, RVA: 0x16e04bd, Size: 0xf000
VA Start: 0x7ffa31401000, RVA: 0x16ef4bd, Size: 0x2000
VA Start: 0x7ffa31403000, RVA: 0x16f14bd, Size: 0x6000
VA Start: 0x7ffa31410000, RVA: 0x16f74bd, Size: 0x1000
VA Start: 0x7ffa31411000, RVA: 0x16f84bd, Size: 0x9000
VA Start: 0x7ffa3141a000, RVA: 0x17014bd, Size: 0x5000
VA Start: 0x7ffa3141f000, RVA: 0x17064bd, Size: 0x2000
VA Start: 0x7ffa31421000, RVA: 0x17084bd, Size: 0x4000
VA Start: 0x7ffa31430000, RVA: 0x170c4bd, Size: 0x1000
VA Start: 0x7ffa31431000, RVA: 0x170d4bd, Size: 0x13000
VA Start: 0x7ffa31444000, RVA: 0x17204bd, Size: 0xc000
VA Start: 0x7ffa31450000, RVA: 0x172c4bd, Size: 0x2000
VA Start: 0x7ffa31452000, RVA: 0x172e4bd, Size: 0x4000
VA Start: 0x7ffa31460000, RVA: 0x17324bd, Size: 0x1000
VA Start: 0x7ffa31461000, RVA: 0x17334bd, Size: 0x2a000
VA Start: 0x7ffa3148b000, RVA: 0x175d4bd, Size: 0x8000
VA Start: 0x7ffa31493000, RVA: 0x17654bd, Size: 0x1000
VA Start: 0x7ffa31494000, RVA: 0x17664bd, Size: 0x6000
VA Start: 0x7ffa314a0000, RVA: 0x176c4bd, Size: 0x1000
VA Start: 0x7ffa314a1000, RVA: 0x176d4bd, Size: 0x16000
VA Start: 0x7ffa314b7000, RVA: 0x17834bd, Size: 0x9000
VA Start: 0x7ffa314c0000, RVA: 0x178c4bd, Size: 0x1000
VA Start: 0x7ffa314c1000, RVA: 0x178d4bd, Size: 0x7000
VA Start: 0x7ffa314d0000, RVA: 0x17944bd, Size: 0x1000
VA Start: 0x7ffa314d1000, RVA: 0x17954bd, Size: 0xe8000
VA Start: 0x7ffa315b9000, RVA: 0x187d4bd, Size: 0x22000
VA Start: 0x7ffa315db000, RVA: 0x189f4bd, Size: 0x1000
VA Start: 0x7ffa315dc000, RVA: 0x18a04bd, Size: 0x1000
VA Start: 0x7ffa315dd000, RVA: 0x18a14bd, Size: 0x7000
VA Start: 0x7ffa315e4000, RVA: 0x18a84bd, Size: 0x1000
VA Start: 0x7ffa315e5000, RVA: 0x18a94bd, Size: 0x11000
VA Start: 0x7ffa31600000, RVA: 0x18ba4bd, Size: 0x1000
VA Start: 0x7ffa31601000, RVA: 0x18bb4bd, Size: 0x3000
VA Start: 0x7ffa31604000, RVA: 0x18be4bd, Size: 0x3000
VA Start: 0x7ffa31607000, RVA: 0x18c14bd, Size: 0x1000
VA Start: 0x7ffa31608000, RVA: 0x18c24bd, Size: 0x4000
VA Start: 0x7ffa31610000, RVA: 0x18c64bd, Size: 0x1000
VA Start: 0x7ffa31611000, RVA: 0x18c74bd, Size: 0xe000
VA Start: 0x7ffa3161f000, RVA: 0x18d54bd, Size: 0x7000
VA Start: 0x7ffa31626000, RVA: 0x18dc4bd, Size: 0x1000
VA Start: 0x7ffa31627000, RVA: 0x18dd4bd, Size: 0x4000
VA Start: 0x7ffa31630000, RVA: 0x18e14bd, Size: 0x1000
VA Start: 0x7ffa31631000, RVA: 0x18e24bd, Size: 0x18000
VA Start: 0x7ffa31649000, RVA: 0x18fa4bd, Size: 0x4000
VA Start: 0x7ffa3164d000, RVA: 0x18fe4bd, Size: 0x1000
VA Start: 0x7ffa3164e000, RVA: 0x18ff4bd, Size: 0x4000
VA Start: 0x7ffa31652000, RVA: 0x19034bd, Size: 0x4000
VA Start: 0x7ffa31660000, RVA: 0x19074bd, Size: 0x1000
VA Start: 0x7ffa31661000, RVA: 0x19084bd, Size: 0x1c000
VA Start: 0x7ffa3167d000, RVA: 0x19244bd, Size: 0xa000
VA Start: 0x7ffa31687000, RVA: 0x192e4bd, Size: 0x1000
VA Start: 0x7ffa31688000, RVA: 0x192f4bd, Size: 0x4000
VA Start: 0x7ffa31690000, RVA: 0x19334bd, Size: 0x1000
VA Start: 0x7ffa31691000, RVA: 0x19344bd, Size: 0x9000
VA Start: 0x7ffa3169a000, RVA: 0x193d4bd, Size: 0x7000
VA Start: 0x7ffa316a1000, RVA: 0x19444bd, Size: 0x1000
VA Start: 0x7ffa316a2000, RVA: 0x19454bd, Size: 0x4000
VA Start: 0x7ffa316b0000, RVA: 0x19494bd, Size: 0x1000
VA Start: 0x7ffa316b1000, RVA: 0x194a4bd, Size: 0x2d000
VA Start: 0x7ffa316de000, RVA: 0x19774bd, Size: 0x13000
VA Start: 0x7ffa316f1000, RVA: 0x198a4bd, Size: 0x2000
VA Start: 0x7ffa316f3000, RVA: 0x198c4bd, Size: 0x6000
VA Start: 0x7ffa31700000, RVA: 0x19924bd, Size: 0x1000
VA Start: 0x7ffa31701000, RVA: 0x19934bd, Size: 0x15000
VA Start: 0x7ffa31716000, RVA: 0x19a84bd, Size: 0x9000
VA Start: 0x7ffa3171f000, RVA: 0x19b14bd, Size: 0x1000
VA Start: 0x7ffa31720000, RVA: 0x19b24bd, Size: 0x3000
VA Start: 0x7ffa31730000, RVA: 0x19b54bd, Size: 0x1000
VA Start: 0x7ffa31731000, RVA: 0x19b64bd, Size: 0x1a000
VA Start: 0x7ffa3174b000, RVA: 0x19d04bd, Size: 0xd000
VA Start: 0x7ffa31758000, RVA: 0x19dd4bd, Size: 0x1000
VA Start: 0x7ffa31759000, RVA: 0x19de4bd, Size: 0x4000
VA Start: 0x7ffa31760000, RVA: 0x19e24bd, Size: 0x1000
VA Start: 0x7ffa31761000, RVA: 0x19e34bd, Size: 0x11000
VA Start: 0x7ffa31772000, RVA: 0x19f44bd, Size: 0x20000
VA Start: 0x7ffa31792000, RVA: 0x1a144bd, Size: 0x1000
VA Start: 0x7ffa31793000, RVA: 0x1a154bd, Size: 0x4000
VA Start: 0x7ffa317a0000, RVA: 0x1a194bd, Size: 0x1000
VA Start: 0x7ffa317a1000, RVA: 0x1a1a4bd, Size: 0x1c000
VA Start: 0x7ffa317bd000, RVA: 0x1a364bd, Size: 0x8000
VA Start: 0x7ffa317c5000, RVA: 0x1a3e4bd, Size: 0x1000
VA Start: 0x7ffa317c6000, RVA: 0x1a3f4bd, Size: 0x8000
VA Start: 0x7ffa317d0000, RVA: 0x1a474bd, Size: 0x1000
VA Start: 0x7ffa317d1000, RVA: 0x1a484bd, Size: 0xa5000
VA Start: 0x7ffa31876000, RVA: 0x1aed4bd, Size: 0x2e000
VA Start: 0x7ffa318a4000, RVA: 0x1b1b4bd, Size: 0x5000
VA Start: 0x7ffa318a9000, RVA: 0x1b204bd, Size: 0x1000
VA Start: 0x7ffa318aa000, RVA: 0x1b214bd, Size: 0x15000
VA Start: 0x7ffa318c0000, RVA: 0x1b364bd, Size: 0x1000
VA Start: 0x7ffa318c1000, RVA: 0x1b374bd, Size: 0x22000
VA Start: 0x7ffa318e3000, RVA: 0x1b594bd, Size: 0x9000
VA Start: 0x7ffa318ec000, RVA: 0x1b624bd, Size: 0x3000
VA Start: 0x7ffa318ef000, RVA: 0x1b654bd, Size: 0x5000
VA Start: 0x7ffa31900000, RVA: 0x1b6a4bd, Size: 0x1000
VA Start: 0x7ffa31901000, RVA: 0x1b6b4bd, Size: 0x126000
VA Start: 0x7ffa31a27000, RVA: 0x1c914bd, Size: 0x4e000
VA Start: 0x7ffa31a75000, RVA: 0x1cdf4bd, Size: 0x9000
VA Start: 0x7ffa31a7e000, RVA: 0x1ce84bd, Size: 0x17000
VA Start: 0x7ffa31aa0000, RVA: 0x1cff4bd, Size: 0x1000
VA Start: 0x7ffa31aa1000, RVA: 0x1d004bd, Size: 0x9000
VA Start: 0x7ffa31aaa000, RVA: 0x1d094bd, Size: 0x4000
VA Start: 0x7ffa31aae000, RVA: 0x1d0d4bd, Size: 0x1000
VA Start: 0x7ffa31aaf000, RVA: 0x1d0e4bd, Size: 0x3000
VA Start: 0x7ffa31b60000, RVA: 0x1d114bd, Size: 0x1000
VA Start: 0x7ffa31b61000, RVA: 0x1d124bd, Size: 0x2000
VA Start: 0x7ffa31b63000, RVA: 0x1d144bd, Size: 0x2000
VA Start: 0x7ffa31b65000, RVA: 0x1d164bd, Size: 0x1000
VA Start: 0x7ffa31b66000, RVA: 0x1d174bd, Size: 0x4000
VA Start: 0x7ffa31b70000, RVA: 0x1d1b4bd, Size: 0x1000
VA Start: 0x7ffa31b71000, RVA: 0x1d1c4bd, Size: 0x38000
VA Start: 0x7ffa31ba9000, RVA: 0x1d544bd, Size: 0x22000
VA Start: 0x7ffa31bcb000, RVA: 0x1d764bd, Size: 0x1000
VA Start: 0x7ffa31bcc000, RVA: 0x1d774bd, Size: 0x2000
VA Start: 0x7ffa31bce000, RVA: 0x1d794bd, Size: 0x1000
VA Start: 0x7ffa31bcf000, RVA: 0x1d7a4bd, Size: 0x7000
VA Start: 0x7ffa31da0000, RVA: 0x1d814bd, Size: 0x1000
VA Start: 0x7ffa31da1000, RVA: 0x1d824bd, Size: 0x9000
VA Start: 0x7ffa31daa000, RVA: 0x1d8b4bd, Size: 0x4000
VA Start: 0x7ffa31dae000, RVA: 0x1d8f4bd, Size: 0x1000
VA Start: 0x7ffa31daf000, RVA: 0x1d904bd, Size: 0x4000
VA Start: 0x7ffa31dc0000, RVA: 0x1d944bd, Size: 0x1000
VA Start: 0x7ffa31dc1000, RVA: 0x1d954bd, Size: 0x13000
VA Start: 0x7ffa31dd4000, RVA: 0x1da84bd, Size: 0xb000
VA Start: 0x7ffa31ddf000, RVA: 0x1db34bd, Size: 0x1000
VA Start: 0x7ffa31de0000, RVA: 0x1db44bd, Size: 0x2d000
VA Start: 0x7ffa31e30000, RVA: 0x1de14bd, Size: 0x1000
VA Start: 0x7ffa31e31000, RVA: 0x1de24bd, Size: 0x12000
VA Start: 0x7ffa31e43000, RVA: 0x1df44bd, Size: 0x8000
VA Start: 0x7ffa31e4b000, RVA: 0x1dfc4bd, Size: 0x1000
VA Start: 0x7ffa31e4c000, RVA: 0x1dfd4bd, Size: 0x5000
VA Start: 0x7ffa31fc0000, RVA: 0x1e024bd, Size: 0x1000
VA Start: 0x7ffa31fc1000, RVA: 0x1e034bd, Size: 0xc3000
VA Start: 0x7ffa32084000, RVA: 0x1ec64bd, Size: 0x3b000
VA Start: 0x7ffa320bf000, RVA: 0x1f014bd, Size: 0x3000
VA Start: 0x7ffa320c2000, RVA: 0x1f044bd, Size: 0xf000
VA Start: 0x7ffa320e0000, RVA: 0x1f134bd, Size: 0x1000
VA Start: 0x7ffa320e1000, RVA: 0x1f144bd, Size: 0x52000
VA Start: 0x7ffa32133000, RVA: 0x1f664bd, Size: 0x3b000
VA Start: 0x7ffa3216e000, RVA: 0x1fa14bd, Size: 0x1000
VA Start: 0x7ffa3216f000, RVA: 0x1fa24bd, Size: 0x3000
VA Start: 0x7ffa32172000, RVA: 0x1fa54bd, Size: 0x8000
VA Start: 0x7ffa32180000, RVA: 0x1fad4bd, Size: 0x1000
VA Start: 0x7ffa32181000, RVA: 0x1fae4bd, Size: 0x116000
VA Start: 0x7ffa32297000, RVA: 0x20c44bd, Size: 0x37000
VA Start: 0x7ffa322ce000, RVA: 0x20fb4bd, Size: 0x7000
VA Start: 0x7ffa322d5000, RVA: 0x21024bd, Size: 0x12000
VA Start: 0x7ffa322f0000, RVA: 0x21144bd, Size: 0x1000
VA Start: 0x7ffa322f1000, RVA: 0x21154bd, Size: 0x194000
VA Start: 0x7ffa32485000, RVA: 0x22a94bd, Size: 0x1c6000
VA Start: 0x7ffa3264b000, RVA: 0x246f4bd, Size: 0x5000
VA Start: 0x7ffa32650000, RVA: 0x24744bd, Size: 0x1000
VA Start: 0x7ffa32651000, RVA: 0x24754bd, Size: 0x4c000
VA Start: 0x7ffa326a0000, RVA: 0x24c14bd, Size: 0x1000
VA Start: 0x7ffa326a1000, RVA: 0x24c24bd, Size: 0x4b000
VA Start: 0x7ffa326ec000, RVA: 0x250d4bd, Size: 0x15000
VA Start: 0x7ffa32701000, RVA: 0x25224bd, Size: 0x2000
VA Start: 0x7ffa32703000, RVA: 0x25244bd, Size: 0x8000
VA Start: 0x7ffa32710000, RVA: 0x252c4bd, Size: 0x1000
VA Start: 0x7ffa32711000, RVA: 0x252d4bd, Size: 0x1b000
VA Start: 0x7ffa3272c000, RVA: 0x25484bd, Size: 0x6000
VA Start: 0x7ffa32732000, RVA: 0x254e4bd, Size: 0x1000
VA Start: 0x7ffa32733000, RVA: 0x254f4bd, Size: 0x5000
VA Start: 0x7ffa32740000, RVA: 0x25544bd, Size: 0x1000
VA Start: 0x7ffa32741000, RVA: 0x25554bd, Size: 0xc000
VA Start: 0x7ffa3274d000, RVA: 0x25614bd, Size: 0x11000
VA Start: 0x7ffa3275e000, RVA: 0x25724bd, Size: 0x1000
VA Start: 0x7ffa3275f000, RVA: 0x25734bd, Size: 0x7000
VA Start: 0x7ffa32770000, RVA: 0x257a4bd, Size: 0x1000
VA Start: 0x7ffa32771000, RVA: 0x257b4bd, Size: 0xa6000
VA Start: 0x7ffa32817000, RVA: 0x26214bd, Size: 0x51000
VA Start: 0x7ffa32868000, RVA: 0x26724bd, Size: 0x5000
VA Start: 0x7ffa3286d000, RVA: 0x26774bd, Size: 0x1c000
VA Start: 0x7ffa32890000, RVA: 0x26934bd, Size: 0x1000
VA Start: 0x7ffa32891000, RVA: 0x26944bd, Size: 0x5c000
VA Start: 0x7ffa328ed000, RVA: 0x26f04bd, Size: 0x18000
VA Start: 0x7ffa32905000, RVA: 0x27084bd, Size: 0x1000
VA Start: 0x7ffa32906000, RVA: 0x27094bd, Size: 0x5000
VA Start: 0x7ffa32910000, RVA: 0x270e4bd, Size: 0x1000
VA Start: 0x7ffa32911000, RVA: 0x270f4bd, Size: 0x68c000
VA Start: 0x7ffa32f9d000, RVA: 0x2d9b4bd, Size: 0x15c000
VA Start: 0x7ffa330f9000, RVA: 0x2ef74bd, Size: 0x8000
VA Start: 0x7ffa33101000, RVA: 0x2eff4bd, Size: 0x1000
VA Start: 0x7ffa33102000, RVA: 0x2f004bd, Size: 0x1000
VA Start: 0x7ffa33103000, RVA: 0x2f014bd, Size: 0x6c000
VA Start: 0x7ffa33400000, RVA: 0x2f6d4bd, Size: 0x1000
VA Start: 0x7ffa33401000, RVA: 0x2f6e4bd, Size: 0xe000
VA Start: 0x7ffa3340f000, RVA: 0x2f7c4bd, Size: 0x14000
VA Start: 0x7ffa33423000, RVA: 0x2f904bd, Size: 0x1000
VA Start: 0x7ffa33424000, RVA: 0x2f914bd, Size: 0x5000
VA Start: 0x7ffa33430000, RVA: 0x2f964bd, Size: 0x1000
VA Start: 0x7ffa33431000, RVA: 0x2f974bd, Size: 0xd5000
VA Start: 0x7ffa33506000, RVA: 0x306c4bd, Size: 0x28000
VA Start: 0x7ffa3352e000, RVA: 0x30944bd, Size: 0x2000
VA Start: 0x7ffa33530000, RVA: 0x30964bd, Size: 0x14000
VA Start: 0x7ffa33550000, RVA: 0x30aa4bd, Size: 0x1000
VA Start: 0x7ffa33551000, RVA: 0x30ab4bd, Size: 0xe2000
VA Start: 0x7ffa33633000, RVA: 0x318d4bd, Size: 0x34000
VA Start: 0x7ffa33667000, RVA: 0x31c14bd, Size: 0x2000
VA Start: 0x7ffa33669000, RVA: 0x31c34bd, Size: 0x1000
VA Start: 0x7ffa3366a000, RVA: 0x31c44bd, Size: 0x8b000
VA Start: 0x7ffa33700000, RVA: 0x324f4bd, Size: 0x1000
VA Start: 0x7ffa33701000, RVA: 0x32504bd, Size: 0x34000
VA Start: 0x7ffa33735000, RVA: 0x32844bd, Size: 0x21000
VA Start: 0x7ffa33756000, RVA: 0x32a54bd, Size: 0x2000
VA Start: 0x7ffa33758000, RVA: 0x32a74bd, Size: 0x6000
VA Start: 0x7ffa338c0000, RVA: 0x32ad4bd, Size: 0x1000
VA Start: 0x7ffa338c1000, RVA: 0x32ae4bd, Size: 0x95000
VA Start: 0x7ffa33956000, RVA: 0x33434bd, Size: 0x23000
VA Start: 0x7ffa33979000, RVA: 0x33664bd, Size: 0x2000
VA Start: 0x7ffa3397b000, RVA: 0x33684bd, Size: 0xf3000
VA Start: 0x7ffa33ef0000, RVA: 0x345b4bd, Size: 0x1000
VA Start: 0x7ffa33ef1000, RVA: 0x345c4bd, Size: 0x73000
VA Start: 0x7ffa33f64000, RVA: 0x34cf4bd, Size: 0x2c000
VA Start: 0x7ffa33f90000, RVA: 0x34fb4bd, Size: 0x4000
VA Start: 0x7ffa33f94000, RVA: 0x34ff4bd, Size: 0x1000
VA Start: 0x7ffa33f95000, RVA: 0x35004bd, Size: 0x1000
VA Start: 0x7ffa33f96000, RVA: 0x35014bd, Size: 0xa000
VA Start: 0x7ffa33fa0000, RVA: 0x350b4bd, Size: 0x1000
VA Start: 0x7ffa33fa1000, RVA: 0x350c4bd, Size: 0x2000
VA Start: 0x7ffa33fa3000, RVA: 0x350e4bd, Size: 0x2000
VA Start: 0x7ffa33fa5000, RVA: 0x35104bd, Size: 0x1000
VA Start: 0x7ffa33fa6000, RVA: 0x35114bd, Size: 0x3000
VA Start: 0x7ffa33fb0000, RVA: 0x35144bd, Size: 0x1000
VA Start: 0x7ffa33fb1000, RVA: 0x35154bd, Size: 0x47000
VA Start: 0x7ffa33ff8000, RVA: 0x355c4bd, Size: 0xe000
VA Start: 0x7ffa34006000, RVA: 0x356a4bd, Size: 0x1000
VA Start: 0x7ffa34007000, RVA: 0x356b4bd, Size: 0x1a000
VA Start: 0x7ffa34140000, RVA: 0x35854bd, Size: 0x1000
VA Start: 0x7ffa34141000, RVA: 0x35864bd, Size: 0x7c000
VA Start: 0x7ffa341bd000, RVA: 0x36024bd, Size: 0x1b000
VA Start: 0x7ffa341d8000, RVA: 0x361d4bd, Size: 0x3000
VA Start: 0x7ffa341db000, RVA: 0x36204bd, Size: 0x2000
VA Start: 0x7ffa341dd000, RVA: 0x36224bd, Size: 0x3000
VA Start: 0x7ffa341e0000, RVA: 0x36254bd, Size: 0x7000
VA Start: 0x7ffa343b0000, RVA: 0x362c4bd, Size: 0x1000
VA Start: 0x7ffa343b1000, RVA: 0x362d4bd, Size: 0x9e000
VA Start: 0x7ffa3444f000, RVA: 0x36cb4bd, Size: 0x26000
VA Start: 0x7ffa34475000, RVA: 0x36f14bd, Size: 0x3000
VA Start: 0x7ffa34478000, RVA: 0x36f44bd, Size: 0xf000
VA Start: 0x7ffa34490000, RVA: 0x37034bd, Size: 0x1000
VA Start: 0x7ffa34491000, RVA: 0x37044bd, Size: 0x81000
VA Start: 0x7ffa34512000, RVA: 0x37854bd, Size: 0x37000
VA Start: 0x7ffa34549000, RVA: 0x37bc4bd, Size: 0x1000
VA Start: 0x7ffa3454a000, RVA: 0x37bd4bd, Size: 0x1000
VA Start: 0x7ffa3454b000, RVA: 0x37be4bd, Size: 0x9000
VA Start: 0x7ffa34630000, RVA: 0x37c74bd, Size: 0x1000
VA Start: 0x7ffa34631000, RVA: 0x37c84bd, Size: 0x6b000
VA Start: 0x7ffa3469c000, RVA: 0x38334bd, Size: 0x38000
VA Start: 0x7ffa346d4000, RVA: 0x386b4bd, Size: 0x5000
VA Start: 0x7ffa346d9000, RVA: 0x38704bd, Size: 0x9000
VA Start: 0x7ffa346f0000, RVA: 0x38794bd, Size: 0x1000
VA Start: 0x7ffa346f1000, RVA: 0x387a4bd, Size: 0x70000
VA Start: 0x7ffa34761000, RVA: 0x38ea4bd, Size: 0x2a000
VA Start: 0x7ffa3478b000, RVA: 0x39144bd, Size: 0x4000
VA Start: 0x7ffa3478f000, RVA: 0x39184bd, Size: 0xa000
VA Start: 0x7ffa347a0000, RVA: 0x39224bd, Size: 0x1000
VA Start: 0x7ffa347a1000, RVA: 0x39234bd, Size: 0x26b000
VA Start: 0x7ffa34a0c000, RVA: 0x3b8e4bd, Size: 0xc7000
VA Start: 0x7ffa34ad3000, RVA: 0x3c554bd, Size: 0x6000
VA Start: 0x7ffa34ad9000, RVA: 0x3c5b4bd, Size: 0x4f000
VA Start: 0x7ffa34bd0000, RVA: 0x3caa4bd, Size: 0x1000
VA Start: 0x7ffa34bd1000, RVA: 0x3cab4bd, Size: 0x131000
VA Start: 0x7ffa34d02000, RVA: 0x3ddc4bd, Size: 0x4e000
VA Start: 0x7ffa34d50000, RVA: 0x3e2a4bd, Size: 0x1000
VA Start: 0x7ffa34d51000, RVA: 0x3e2b4bd, Size: 0x2000
VA Start: 0x7ffa34d53000, RVA: 0x3e2d4bd, Size: 0x9000
VA Start: 0x7ffa34d5c000, RVA: 0x3e364bd, Size: 0x8b000
```
