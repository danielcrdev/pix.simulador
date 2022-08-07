{
    "Envelope": {
        "@xmlns": "https://www.bcb.gov.br/pi/pacs.008/1.8",
        "AppHdr": {
            "BizMsgIdr": "M92894922MO85C0g1jrPjlwH51e2Cow8",
            "CreDt": "2022-07-31T13:23:15.777Z",
            "Fr": {
                "FIId": {
                    "FinInstnId": {
                        "Othr": {
                            "Id": "92894922"
                        }
                    }
                }
            },
            "MsgDefIdr": "pacs.008.spi.1.8",
            "Sgntr": {
                "ds:Signature": {
                    "@xmlns:ds": "http://www.w3.org/2000/09/xmldsig#",
                    "ds:KeyInfo": {
                        "@Id": "C910E304BB60B99DA53FCCFC76891E03",
                        "ds:X509Data": {
                            "ds:X509IssuerSerial": {
                                "ds:X509IssuerName": "CN=SERASA Autoridade Certificadora v5, OU=CSPB-4, O=ICP-Brasil, C=BR",
                                "ds:X509SerialNumber": "2228078329512312233"
                            }
                        }
                    },
                    "ds:SignatureValue": "dOm/FYcW9Jht33/MPqQdtbLxatocLEJBgsnt03AFfIGEgxsW2jZO0yoqcjA7up2l\nAjJ3JVL4KW0btuQRFUo2jjCdWUttoRbjX0PwZSHa34II24LUZ34SI4n+GjYJLwj0\nNVUBjQDXjA7Erm+DJ0AVKkCIvAj+5Pj47S6Wi3lhiqq/aEwrtVXQCrikYpAtSUa+\n4XruaxYQiZ6v/ajHZez8Z4QIApzCOH4jyWd/U9k4HtBoMP/K1UUO0isoPKnc67TL\nnXTPR4k/pYUjjJ4Wa28Bu48qtCyxE+k9D4Wko3CgM1fhxkdRlvY/B/ybnRtNuCBj\nHFxTuv4Chp8piPDIG7rNtQ==",
                    "ds:SignedInfo": {
                        "ds:CanonicalizationMethod": {
                            "@Algorithm": "http://www.w3.org/2001/10/xml-exc-c14n#"
                        },
                        "ds:Reference": [
                            {
                                "@URI": "#C910E304BB60B99DA53FCCFC76891E03",
                                "ds:DigestMethod": {
                                    "@Algorithm": "http://www.w3.org/2001/04/xmlenc#sha256"
                                },
                                "ds:DigestValue": "UZoCh9vQHEe+zgGwWLvkspulJDge3Lk+G0sA5INrjyk=",
                                "ds:Transforms": {
                                    "ds:Transform": {
                                        "@Algorithm": "http://www.w3.org/2001/10/xml-exc-c14n#"
                                    }
                                }
                            },
                            {
                                "@URI": "",
                                "ds:DigestMethod": {
                                    "@Algorithm": "http://www.w3.org/2001/04/xmlenc#sha256"
                                },
                                "ds:DigestValue": "SnjUJNZgcHBC7h1PwI3LLQNqnok4N95obeuJKnvcQ2I=",
                                "ds:Transforms": {
                                    "ds:Transform": [
                                        {
                                            "@Algorithm": "http://www.w3.org/2000/09/xmldsig#enveloped-signature"
                                        },
                                        {
                                            "@Algorithm": "http://www.w3.org/2001/10/xml-exc-c14n#"
                                        }
                                    ]
                                }
                            },
                            {
                                "ds:DigestMethod": {
                                    "@Algorithm": "http://www.w3.org/2001/04/xmlenc#sha256"
                                },
                                "ds:DigestValue": "1U66nhqAWLYYAQNf/kKqXU1rPb3IFo0uTYLXkuxLKp8=",
                                "ds:Transforms": {
                                    "ds:Transform": {
                                        "@Algorithm": "http://www.w3.org/2001/10/xml-exc-c14n#"
                                    }
                                }
                            }
                        ],
                        "ds:SignatureMethod": {
                            "@Algorithm": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
                        }
                    }
                }
            },
            "To": {
                "FIId": {
                    "FinInstnId": {
                        "Othr": {
                            "Id": "00038166"
                        }
                    }
                }
            }
        },
        "Document": {
            "FIToFICstmrCdtTrf": {
                "CdtTrfTxInf": {
                    "AccptncDtTm": "2022-07-31T13:23:15.370Z",
                    "Cdtr": {
                        "Id": {
                            "PrvtId": {
                                "Othr": {
                                    "Id": "45292105880"
                                }
                            }
                        }
                    },
                    "CdtrAcct": {
                        "Id": {
                            "Othr": {
                                "Id": "117675334",
                                "Issr": "1"
                            }
                        },
                        "Prxy": {
                            "Id": "thainaribeiro2016@outlook.com"
                        },
                        "Tp": {
                            "Cd": "CACC"
                        }
                    },
                    "CdtrAgt": {
                        "FinInstnId": {
                            "ClrSysMmbId": {
                                "MmbId": "00416968"
                            }
                        }
                    },
                    "ChrgBr": "SLEV",
                    "Dbtr": {
                        "Id": {
                            "PrvtId": {
                                "Othr": {
                                    "Id": "42477397869"
                                }
                            }
                        },
                        "Nm": "RODRIGO CAVALHEIRO LIMA"
                    },
                    "DbtrAcct": {
                        "Id": {
                            "Othr": {
                                "Id": "44089643",
                                "Issr": "1"
                            }
                        },
                        "Tp": {
                            "Cd": "CACC"
                        }
                    },
                    "DbtrAgt": {
                        "FinInstnId": {
                            "ClrSysMmbId": {
                                "MmbId": "92894922"
                            }
                        }
                    },
                    "IntrBkSttlmAmt": {
                        "#text": "2.61",
                        "@Ccy": "BRL"
                    },
                    "MndtRltdInf": {
                        "Tp": {
                            "LclInstrm": {
                                "Prtry": "DICT"
                            }
                        }
                    },
                    "PmtId": {
                        "EndToEndId": "E92894922202207311323035142A5TD4"
                    },
                    "Purp": {
                        "Cd": "IPAY"
                    }
                },
                "GrpHdr": {
                    "CreDtTm": "2022-07-31T13:23:15.777Z",
                    "MsgId": "M92894922MO85C0g1jrPjlwH51e2Cow8",
                    "NbOfTxs": "1",
                    "PmtTpInf": {
                        "InstrPrty": "HIGH",
                        "SvcLvl": {
                            "Prtry": "PAGPRI"
                        }
                    },
                    "SttlmInf": {
                        "SttlmMtd": "CLRG"
                    }
                }
            }
        }
    }
}