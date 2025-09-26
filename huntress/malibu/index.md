+++
title = "Malibu"
description = "What do you bring to the beach?"
authors = ["cstef"]
date = 2024-09-30

[taxonomies]
categories = ["misc"]
+++

## Description

What do you bring to the beach?

----

We are given a host and port, by `nc`-ing into it, we see that it is in fact just an HTTP "proxy": we can send raw HTTP requests and the result is then returned.

After trying `GET`-ing `/`, `/malibu`, ..., we notice in the headers that the server is running [`minio`](https://github.com/minio/minio), an S3-compatible service.

Thinking about the challenge's description: "What do you bring to the beach?", I start to enumerate things people would take with them to the beach: sunscreen, shovel, bucket...? That's gotta be it, a (S3) bucket !

By `GET`-ing `/bucket`, we effectively get a list of all the files stored, with their respective ids:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Name>bucket</Name>
    <Prefix></Prefix>
    <Marker></Marker>
    <MaxKeys>1000</MaxKeys>
    <IsTruncated>false</IsTruncated>
    <Contents>
        <Key>11CUZe0s/X1P4LzhV/P4EiYz4H/Nq8coOg8/sRQlYZolbeSB4tFm</Key>
        <LastModified>2024-10-04T20:57:51.317Z</LastModified>
        <ETag>&#34;f58d31146509e5baa283f8f881c9b64a&#34;</ETag>
        <Size>2216</Size>
        <Owner>
            <ID>02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4</ID>
            <DisplayName>minio</DisplayName>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    <Contents>
        <Key>MzsbOdN2/63idswdq/lEFnRMRX/YnKgkLtQ86mdY0qr</Key>
        <LastModified>2024-10-04T20:57:40.219Z</LastModified>
        <ETag>&#34;196857245d35acd3ff29cade123d7159&#34;</ETag>
        <Size>1139</Size>
        <Owner>
            <ID>02d6176db174dc93cb1b899f7c6078f08654445fe8cf1b6ce98d8855f66bdbf4</ID>
            <DisplayName>minio</DisplayName>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
    </Contents>
    ...
</ListBucketResult>
```

And so, we retrieve the contents of each file with their respective URL `/bucket/KEY`.

We get a bunch of nonsensical data, at this point I tried decoding it in I-don't-know-how-many ways, only to find that the flag was simply hidden in cleartext in the middle of one of the files... Flagged...

```bash
rg "flag\\{.*\\}" responses/ -o
# responses/stTxquhE_Q85W77Y5_6f4pIhLlhojSLGs3
# 1:flag{800e6603e86fe0a68875d3335e0daf81}
```