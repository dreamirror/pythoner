using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data;
using System.Data.OleDb;
using NPOI;
using NPOI.HPSF;
using NPOI.HSSF;
using NPOI.HSSF.UserModel;
using NPOI.POIFS;
using NPOI.Util;
using NPOI.HSSF.Util;
using NPOI.HSSF.Extractor;
using System.IO;
namespace Excel
{
    public partial class Form1 : Form
    {
        HSSFWorkbook HBook;
        public Form1()
        {
            InitializeComponent();
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            
        }

        private void folderBrowserDialog1_HelpRequest(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyComputer);
            openFileDialog.Filter = "Excel文件(*.xls)|*.xls|所有文件(*.*)|*.*";
            
            if (openFileDialog.ShowDialog(this) == DialogResult.OK)
            {
                string FileName = openFileDialog.FileName;
                label1.Text = FileName;
                List<string> sheet_names = new List<string>();
                FileInfo fi = new FileInfo(FileName);
                if (fi.Exists == true)
                {
                    using (FileStream fs = fi.Open(FileMode.Open))
                    {
                        HBook = new HSSFWorkbook(fs);
                        int sheet_num = HBook.NumberOfSheets;
                        for (int i = 0; i < sheet_num; ++i) {
                            HSSFSheet sheet = (HSSFSheet)HBook.GetSheetAt(i);
                            sheet_names.Add(sheet.SheetName);
                        }
                        set_comboBox(sheet_names);

                    }
                }

            }

        }



        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void create_sheet_lable(String name) {
            Console.WriteLine(name);
        }

        private void tabPage1_Click(object sender, EventArgs e)
        {

        }

        private void set_comboBox(List<string> names){
            foreach (var name in names) {
                comboBox1.Items.Add(name);
            }
            comboBox1.SelectedIndex = 0;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            dataGridView1.DataSource = null;

            HSSFSheet sheet = (HSSFSheet)HBook.GetSheetAt(comboBox1.SelectedIndex);
            var row1 = sheet.GetRow(1);
            var col_num1 = row1.LastCellNum;
            DataTable dt = new DataTable();
            for (var i = 0; i < col_num1; ++i)
            {
                DataColumn c = new DataColumn("",typeof(string));
                dt.Columns.Add(c);
            }
            dataGridView1.DataSource = dt.DefaultView;
            var row_num = sheet.LastRowNum;
            Console.WriteLine(row_num);
            for (var i = 0; i < row_num; ++i) { 
                var row = sheet.GetRow(i);
                var col_num = 0;
                try
                {
                    col_num = row.LastCellNum;
                }
                catch (Exception e1)
                {
                }
      
                DataRow dr = dt.NewRow();
                for (var j = 0; j < col_num; ++j)
                {
                    dr[j] = row.GetCell(j);
                }
                dt.Rows.Add(dr);
            }

            dataGridView1.Rows[3].Cells[2].Style.ForeColor = Color.Red;

        }
      

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridView1_CellContentClick_1(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Console.WriteLine("11111");
        }

    }
}
