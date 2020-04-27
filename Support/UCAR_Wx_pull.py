# python script to download selected files from rda.ucar.edu
#
import sys
import os
import urllib3
import http.cookiejar as cookielib

if len(sys.argv) != 2:
    print("usage: " + sys.argv[0] + " [-q] password_on_RDA_webserver")
    print("-q suppresses the progress message for each file that is downloaded")
    sys.exit(1)
#
passwd_idx = 1
verbose = True
if len(sys.argv) == 3 and sys.argv[1] == "-q":
    passwd_idx = 2
    verbose = False
#
cj = cookielib.MozillaCookieJar()
opener = urllib3.build_opener(urllib3.HTTPCookieProcessor(cj))
#
# check for existing cookies file and authenticate if necessary
do_authentication = False
if os.path.isfile("auth.rda.ucar.edu"):
    cj.load("auth.rda.ucar.edu", False, True)
    for cookie in cj:
        if (cookie.name == "sess" and cookie.is_expired()):
            do_authentication = True
else:
    do_authentication = True
if do_authentication:
    login = opener.open("https://rda.ucar.edu/cgi-bin/login",
                        "email=ckw08@my.fsu.edu&password=" + sys.argv[1] + "&action=login")
    #
    # save the authentication cookies for future downloads NOTE! - cookies are saved for future sessions because 
    # overly-frequent authentication to our server can cause your data access to be blocked 
    cj.clear_session_cookies()
    cj.save("auth.rda.ucar.edu", True, True)
#
# download the data file(s)
listoffiles = ["ec.oper.an.sfc/201810/ec.oper.an.sfc.128_164_tcc.regn1280sc.20181001.grb",
               "ec.oper.an.sfc/201810/ec.oper.an.sfc.128_186_lcc.regn1280sc.20181001.grb",
               "ec.oper.an.sfc/201810/ec.oper.an.sfc.128_187_mcc.regn1280sc.20181001.grb",
               "ec.oper.an.sfc/201810/ec.oper.an.sfc.128_188_hcc.regn1280sc.20181001.grb",
               "ec.oper.an.sfc/201810/ec.oper.an.sfc.128_164_tcc.regn1280sc.20181002.grb",
               "ec.oper.an.sfc/201810/ec.oper.an.sfc.128_186_lcc.regn1280sc.20181002.grb",
               "ec.oper.an.sfc/201810/ec.oper.an.sfc.128_187_mcc.regn1280sc.20181002.grb",
               "ec.oper.an.sfc/201810/ec.oper.an.sfc.128_188_hcc.regn1280sc.20181002.grb"]
for file in listoffiles:
    idx = file.rfind("/")
    if idx > 0:
        ofile = file[idx + 1:]
    else:
        ofile = file
    if verbose:
        sys.stdout.write("downloading " + ofile + "...")
        sys.stdout.flush()
    infile = opener.open("http://rda.ucar.edu/data/ds113.1/" + file)
    outfile = open(ofile, "wb")
    outfile.write(infile.read())
    outfile.close()
    if verbose:
        sys.stdout.write("done.\n")
