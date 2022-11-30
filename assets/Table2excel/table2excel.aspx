<%@ Page Language="C#" AutoEventWireup="true" CodeFile="table2excel.aspx.cs" Inherits="Account_Table2excel_table2excel" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <script src="jquery.min.1.11.1.js" type="text/javascript"></script>
    <script src="jquery.table2excel.min.js" type="text/javascript"></script>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <table id="mytable" cellpadding="5" border="1" cellspacing="0">
            <thead>
                <tr>
                    <th>
                        Employee Name
                    </th>
                    <th>
                        Age
                    </th>
                    <th>
                        Designation
                    </th>
                    <th>
                        Experience
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        Rajeev
                    </td>
                    <td>
                        31
                    </td>
                    <td>
                        Developer
                    </td>
                    <td>
                        6
                    </td>
                </tr>
                <tr>
                    <td>
                        Sandhya
                    </td>
                    <td>
                        27
                    </td>
                    <td>
                        Tester
                    </td>
                    <td>
                        2
                    </td>
                </tr>
                <tr>
                    <td>
                        Ramesh
                    </td>
                    <td>
                        25
                    </td>
                    <td>
                        Designer
                    </td>
                    <td>
                        1
                    </td>
                </tr>
                <tr>
                    <td>
                        Sanjay
                    </td>
                    <td>
                        32
                    </td>
                    <td>
                        Developer
                    </td>
                    <td>
                        5
                    </td>
                </tr>
                <tr>
                    <td>
                        Ramya
                    </td>
                    <td>
                        23
                    </td>
                    <td>
                        Developer
                    </td>
                    <td>
                        1
                    </td>
                </tr>
            </tbody>
        </table>
        <br />
        <button onclick="exportexcel()">
            Export to Excel</button>
        <script type="text/javascript">
            function exportexcel() {
                $("#mytable").table2excel({
                    name: "Table2Excel",
                    filename: "myFileName",
                    fileext: ".xls"
                });
            }
		</script>
    </div>
    </form>
</body>
</html>
