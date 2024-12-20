# -*- coding: utf-8 -*-

from system_tests import CaseMeta, CopyTmpFiles, path
@CopyTmpFiles("$data_path/issue_ghsa_mxw9_qx4c_6m8v_poc.jp2")

class Jp2ImageEncodeJp2HeaderOutOfBoundsRead2(metaclass=CaseMeta):
    """
    Regression test for the bug described in:
    https://github.com/Exiv2/exiv2/security/advisories/GHSA-mxw9-qx4c-6m8v
    """
    url = "https://github.com/Exiv2/exiv2/security/advisories/GHSA-mxw9-qx4c-6m8v"

    filename = path("$tmp_path/issue_ghsa_mxw9_qx4c_6m8v_poc.jp2")
    commands = ["$exiv2 rm $filename"]
    stdout = [""]
    stderr = [
        """$exception_in_erase """ + filename + """:
$kerCorruptedMetadata
"""]
    retval = [1]
