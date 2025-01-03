import json


field_types = {
    "bigint": "int64",
    "smallint": "int32",
    "varchar(65535)": "string",
    "timestamp": "timestamp",
    "date": "date",
    "int": "int32"
}


fields = [
    ("watchid", "bigint"),
    ("javaenable", "smallint"),
    ("title", "varchar(65535)"),
    ("goodevent", "smallint"),
    ("eventtime", "timestamp"),
    ("eventdate", "date"),
    ("counterid", "int"),
    ("clientip", "int"),
    ("regionid", "int"),
    ("userid", "bigint"),
    ("counterclass", "smallint"),
    ("os", "smallint"),
    ("useragent", "smallint"),
    ("url", "varchar(65535)"),
    ("referer", "varchar(65535)"),
    ("isrefresh", "smallint"),
    ("referercategoryid", "smallint"),
    ("refererregionid", "int"),
    ("urlcategoryid", "smallint"),
    ("urlregionid", "int"),
    ("resolutionwidth", "smallint"),
    ("resolutionheight", "smallint"),
    ("resolutiondepth", "smallint"),
    ("flashmajor", "smallint"),
    ("flashminor", "smallint"),
    ("flashminor2", "varchar(65535)"),
    ("netmajor", "smallint"),
    ("netminor", "smallint"),
    ("useragentmajor", "smallint"),
    ("useragentminor", "varchar(65535)"),
    ("cookieenable", "smallint"),
    ("javascriptenable", "smallint"),
    ("ismobile", "smallint"),
    ("mobilephone", "smallint"),
    ("mobilephonemodel", "varchar(65535)"),
    ("params", "varchar(65535)"),
    ("ipnetworkid", "int"),
    ("traficsourceid", "smallint"),
    ("searchengineid", "smallint"),
    ("searchphrase", "varchar(65535)"),
    ("advengineid", "smallint"),
    ("isartifical", "smallint"),
    ("windowclientwidth", "smallint"),
    ("windowclientheight", "smallint"),
    ("clienttimezone", "smallint"),
    ("clienteventtime", "timestamp"),
    ("silverlightversion1", "smallint"),
    ("silverlightversion2", "smallint"),
    ("silverlightversion3", "int"),
    ("silverlightversion4", "smallint"),
    ("pagecharset", "varchar(65535)"),
    ("codeversion", "int"),
    ("islink", "smallint"),
    ("isdownload", "smallint"),
    ("isnotbounce", "smallint"),
    ("funiqid", "bigint"),
    ("originalurl", "varchar(65535)"),
    ("hid", "int"),
    ("isoldcounter", "smallint"),
    ("isevent", "smallint"),
    ("isparameter", "smallint"),
    ("dontcounthits", "smallint"),
    ("withhash", "smallint"),
    ("hitcolor", "varchar(65535)"),
    ("localeventtime", "timestamp"),
    ("age", "smallint"),
    ("sex", "smallint"),
    ("income", "smallint"),
    ("interests", "smallint"),
    ("robotness", "smallint"),
    ("remoteip", "int"),
    ("windowname", "int"),
    ("openername", "int"),
    ("historylength", "smallint"),
    ("browserlanguage", "varchar(65535)"),
    ("browsercountry", "varchar(65535)"),
    ("socialnetwork", "varchar(65535)"),
    ("socialaction", "varchar(65535)"),
    ("httperror", "smallint"),
    ("sendtiming", "int"),
    ("dnstiming", "int"),
    ("connecttiming", "int"),
    ("responsestarttiming", "int"),
    ("responseendtiming", "int"),
    ("fetchtiming", "int"),
    ("socialsourcenetworkid", "smallint"),
    ("socialsourcepage", "varchar(65535)"),
    ("paramprice", "bigint"),
    ("paramorderid", "varchar(65535)"),
    ("paramcurrency", "varchar(65535)"),
    ("paramcurrencyid", "smallint"),
    ("openstatservicename", "varchar(65535)"),
    ("openstatcampaignid", "varchar(65535)"),
    ("openstatadid", "varchar(65535)"),
    ("openstatsourceid", "varchar(65535)"),
    ("utmsource", "varchar(65535)"),
    ("utmmedium", "varchar(65535)"),
    ("utmcampaign", "varchar(65535)"),
    ("utmcontent", "varchar(65535)"),
    ("utmterm", "varchar(65535)"),
    ("fromtag", "varchar(65535)"),
    ("hasgclid", "smallint"),
    ("refererhash", "bigint"),
    ("urlhash", "bigint"),
    ("clid", "int")
]


converted_names=[field[0] for field in fields]
converted_types = [field_types.get(field[1], field[1]) for field in fields]


output = {
    "schema": {
        "hits": converted_types
    }
}
print(converted_names)
print(converted_types)

output_names={
    "columnNames":{
        "hits":converted_names
    }
}

print(json.dumps(output_names,indent=2))
print(json.dumps(output, indent=2))
