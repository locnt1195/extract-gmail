[
    {'name': 'Delivered-To', 'value': 'locnt1195@gmail.com'},
    {
        'name': 'Received',
        'value': 'by 2002:a05:7000:5890:b0:58e:4445:a04 with SMTP id h16csp934647max;        Fri, 31 May 2024 23:48:13 -0700 (PDT)',
    },
    {
        'name': 'X-Google-Smtp-Source',
        'value': 'AGHT+IEr35JsUcJNMHRze4ncKboOSYZPPCmGNNcO/ppZ7nkURrHTXtVw/NGhdVxwN23SKrHIOtPW',
    },
    {
        'name': 'X-Received',
        'value': 'by 2002:a05:6808:1453:b0:3c9:9398:4c7e with SMTP id 5614622812f47-3d1e3476695mr4257782b6e.6.1717224492945;        Fri, 31 May 2024 23:48:12 -0700 (PDT)',
    },
    {
        'name': 'ARC-Seal',
        'value': 'i=1; a=rsa-sha256; t=1717224492; cv=none;        d=google.com; s=arc-20160816;        b=hUFKulzeFpplfE/Pb0n3pB9u4KnL97suqsWfpA5Qrn5qeIY2aCgw601lHb4GIL35L5         Vw1gs9oNvQjESKE95OreoZ2CcirC/7lahsr4s5ZFlaJn61ogPDdJntHoZ/AgfA6JVZ4d         l7Rk7QNsebXAEesXvHJ3A8PHN7gSnSOVMs1dvLbpeDuntBiYvj7NM+3UZEEFlJeqiDns         QwGTch14ISySyAu0UVeSK/TqAtrTn+lHGguTR858r/gO/4vZ1ylwxh1mMuY/dxin6TVT         yoC6r2eubfwt+ItwlhIOIaLUmvuOdgscuSCSxyr+7lolFpvOYuNG8/T6/yZs3w4lUcX9         TjIw==',
    },
    {
        'name': 'ARC-Message-Signature',
        'value': 'i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=destinations:list-unsubscribe-post:list-unsubscribe:list-post         :list-archive:list-id:precedence:content-transfer-encoding         :mime-version:subject:references:in-reply-to:message-id:cc:to         :reply-to:from:date:dkim-signature;        bh=sG2csf8jHT9Z13k84+18j5eUyBuOZ6i7gaB/HSU3Huw=;        fh=ntvsNKhMA+1OTpsRtfKcskP+YgMe+gd7YpYcs2b94z8=;        b=zwIz24S2JHsvy2w3AsKVXkmNVxiSUKELs5YFM+Q2sb8y3jwPGoQGTpqNFAwPNxttK+         SEKSo9a+ATX5OdnSAiaFVIMKy5T3V//qt+kPH2ssBHwd3qEXmmGF28HS6gP6c4IPL8C+         w3iqz43Y1/RNwkjJKR0kfxqMuvCwUF0krZNnps7GUhspMBcwsNac70Xr4ygCrwldgme+         YyyY4d/YQbbmGjD+SHjdDTLsiCXj1gZBzoQIWNMxDQRIGZQmtq+gWbkGrFS33Dlwg6EP         A9yiz4M18Rl6f6XNRv3u5IMJZBG6FW26nRV2MQP2MQrBzU1/svo44d7Cb2Duh1kqmmQH         FxYw==;        dara=google.com',
    },
    {
        'name': 'ARC-Authentication-Results',
        'value': 'i=1; mx.google.com;       dkim=pass header.i=@github.com header.s=pf2023 header.b=AAjyKH5c;       spf=pass (google.com: domain of noreply@github.com designates 192.30.252.207 as permitted sender) smtp.mailfrom=noreply@github.com;       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=github.com',
    },
    {'name': 'Return-Path', 'value': '<noreply@github.com>'},
    {
        'name': 'Received',
        'value': 'from out-24.smtp.github.com (out-24.smtp.github.com. [192.30.252.207])        by mx.google.com with ESMTPS id 6a1803df08f44-6ae4b42b750si38734276d6.475.2024.05.31.23.48.12        for <locnt1195@gmail.com>        (version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);        Fri, 31 May 2024 23:48:12 -0700 (PDT)',
    },
    {
        'name': 'Received-SPF',
        'value': 'pass (google.com: domain of noreply@github.com designates 192.30.252.207 as permitted sender) client-ip=192.30.252.207;',
    },
    {
        'name': 'Authentication-Results',
        'value': 'mx.google.com;       dkim=pass header.i=@github.com header.s=pf2023 header.b=AAjyKH5c;       spf=pass (google.com: domain of noreply@github.com designates 192.30.252.207 as permitted sender) smtp.mailfrom=noreply@github.com;       dmarc=pass (p=REJECT sp=REJECT dis=NONE) header.from=github.com',
    },
    {
        'name': 'Received',
        'value': 'from github.com (hubbernetes-node-eaaf49b.ac4-iad.github.net [10.52.211.57]) by smtp.github.com (Postfix) with ESMTPA id 9A3BB640A6C for <locnt1195@gmail.com>; Fri, 31 May 2024 23:48:12 -0700 (PDT)',
    },
    {
        'name': 'DKIM-Signature',
        'value': 'v=1; a=rsa-sha256; c=relaxed/relaxed; d=github.com; s=pf2023; t=1717224492; bh=sG2csf8jHT9Z13k84+18j5eUyBuOZ6i7gaB/HSU3Huw=; h=Date:From:Reply-To:To:Cc:In-Reply-To:References:Subject:List-ID:\t List-Archive:List-Post:List-Unsubscribe:List-Unsubscribe-Post:\t From; b=AAjyKH5cZt4geoFz6h2A2jsAzH9hGCx4B8+6fo5qVc3PfnvoFVovMAgF6O6ups9WO\t 5lCF4ZZ9C6atgn8cUgCQAdzn6ZBpibXC4l+FM6EIdlrQpiUwuaQSSouvPuYIKFRIqP\t cCh76uFqIgL89HpRGvWfLUcfgJ2zdWYMSsAkuZ44=',
    },
    {'name': 'Date', 'value': 'Fri, 31 May 2024 23:48:12 -0700'},
    {'name': 'From', 'value': 'Anh Vu <notifications@github.com>'},
    {
        'name': 'Reply-To',
        'value': '"anhvu-sg/odoo-walker-supply-co" <reply+AEKKPMUWEFWK6G45YIKI3KGEM2SSZEVBNHHIVUJGDU@reply.github.com>',
    },
    {'name': 'To', 'value': '"anhvu-sg/odoo-walker-supply-co" <odoo-walker-supply-co@noreply.github.com>'},
    {'name': 'Cc', 'value': 'Nguyen Thanh Loc <locnt1195@gmail.com>, Author <author@noreply.github.com>'},
    {'name': 'Message-ID', 'value': '<anhvu-sg/odoo-walker-supply-co/pull/11/issue_event/13008351675@github.com>'},
    {'name': 'In-Reply-To', 'value': '<anhvu-sg/odoo-walker-supply-co/pull/11@github.com>'},
    {'name': 'References', 'value': '<anhvu-sg/odoo-walker-supply-co/pull/11@github.com>'},
    {'name': 'Subject', 'value': 'Re: [anhvu-sg/odoo-walker-supply-co] Fix preview youtube url (PR #11)'},
    {'name': 'Mime-Version', 'value': '1.0'},
    {
        'name': 'Content-Type',
        'value': 'multipart/alternative; boundary="--==_mimepart_665ac42c98303_9918602315f8"; charset=UTF-8',
    },
    {'name': 'Content-Transfer-Encoding', 'value': '7bit'},
    {'name': 'Precedence', 'value': 'list'},
    {'name': 'X-GitHub-Sender', 'value': 'anhvu-sg'},
    {'name': 'X-GitHub-Recipient', 'value': 'locnt1195'},
    {'name': 'X-GitHub-Reason', 'value': 'author'},
    {'name': 'List-ID', 'value': 'anhvu-sg/odoo-walker-supply-co <odoo-walker-supply-co.anhvu-sg.github.com>'},
    {'name': 'List-Archive', 'value': 'https://github.com/anhvu-sg/odoo-walker-supply-co'},
    {'name': 'List-Post', 'value': '<mailto:reply+AEKKPMUWEFWK6G45YIKI3KGEM2SSZEVBNHHIVUJGDU@reply.github.com>'},
    {
        'name': 'List-Unsubscribe',
        'value': '<mailto:unsub+AEKKPMUWEFWK6G45YIKI3KGEM2SSZEVBNHHIVUJGDU@reply.github.com>, <https://github.com/notifications/unsubscribe/one-click/AEKKPMWLSRMOYPIKLACWVYLZFFVCZANCNFSM6AAAAABIT45TI4>',
    },
    {'name': 'List-Unsubscribe-Post', 'value': 'List-Unsubscribe=One-Click'},
    {'name': 'X-Auto-Response-Suppress', 'value': 'All'},
    {'name': 'destinations', 'value': 'locnt1195@gmail.com'},
    {'name': 'X-GitHub-Recipient-Address', 'value': 'locnt1195@gmail.com'},
]
