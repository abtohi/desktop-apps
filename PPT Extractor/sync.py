import pandas as pd
import subprocess
from ttkbootstrap.dialogs import Messagebox

class Synchronize:
    def __init__(self, root, lbl_status, dtype, progress, progress_var, frame, dtable, projectpath):
        self.root = root
        self.lbl_status = lbl_status
        self.dtype = dtype
        self.progress = progress
        self.progress_var = progress_var
        self.frame = frame
        self.dtable = dtable
        self.projectpath = f'projects\{projectpath.get()}'

    def sync(self):
        cnv = f'{self.projectpath}\output\converted_data.xlsx'
        self.sync_all(cnv)
        
        self.lbl_status.config(text="You have successfully syncrhonized the data table to your converted data")
        result = Messagebox.yesno(title="Options",message="Your data has been successfully synchronized to "+cnv+"\n\nDo you want to open the output?",parent=self.frame)
        if result == 'Yes':
            subprocess.run(['start', 'excel', cnv], shell=True)
        self.progress.pack_forget()

    def sync_texts(self,cnv):
        self.lbl_status.config(text="Synchronizing Texts")
        self.root.update_idletasks()
        table_filename = self.dtable
        rev_filename = cnv
        self.sync_engine(table_filename, rev_filename)

    def sync_tables(self,cnv):
        self.lbl_status.config(text="Synchronizing Tables")
        self.root.update_idletasks()
        table_filename = self.dtable
        rev_filename = cnv
        self.sync_engine(table_filename, rev_filename)
    
    def sync_charts(self, cnv):
        self.lbl_status.config(text="Synchronizing Charts")
        self.root.update_idletasks()
        table_filename = self.dtable
        rev_filename = cnv
        self.sync_engine(table_filename, rev_filename)

    def sync_all(self, cnv):
        if 'Texts' in self.dtype:
            self.sync_texts(cnv)
        if 'Tables' in self.dtype:
            self.sync_tables(cnv)
        if 'Charts' in self.dtype:
            self.sync_charts(cnv)
        
    def sync_engine(self,toc,rev):
        self.lbl_status.config(text="Opening the Converted File")
        self.root.update_idletasks()
        df_conv = pd.read_excel(rev)
        self.lbl_status.config(text="Opening the Data Table")
        self.root.update_idletasks()
        df_tab = pd.read_excel(toc,sheet_name=None)
        toc = df_tab['TOC']

        with pd.ExcelWriter(rev, engine='xlsxwriter') as writer:
            new_df = []
            for i,conv in df_conv.iterrows():
                self.progress_var.set(i+1 / len(df_conv) * 100)
                self.root.update_idletasks()
                slide = conv.iloc[0]
                obj = conv.iloc[1]
                size = conv.iloc[2]
                index = conv.iloc[3]
                header = conv.iloc[4]
                categories = conv.iloc[5]
                ppt_value = conv.iloc[6]
                key_ques = '' if str(conv.iloc[8]) == 'nan' else conv.iloc[8]
                key_resp = '' if str(conv.iloc[9]) == 'nan' else conv.iloc[9]
                key_head = '' if str(conv.iloc[10]) == 'nan' else conv.iloc[10]
                tipe = conv.iloc[11]
                info = conv.iloc[12]
                
                n = False
                if str(conv.iloc[8]) !='nan':
                    keyQ = conv.iloc[8]
                    keyR = conv.iloc[5] if str(conv.iloc[9]) == 'nan' else str(conv.iloc[9]).replace('\n',' ')
                    keyH = str(conv.iloc[4]).replace('\n',' ') if str(conv.iloc[10]) == 'nan' else str(conv.iloc[10]).replace('\n',' ')
                    for j, tab in toc.iterrows():
                        if keyQ == tab.iloc[4]:
                            dtable = df_tab[tab.iloc[0]]
                            dtable = dtable.drop([0, 1])
                            new_header = dtable.iloc[0].str.replace('\n',' ')
                            dtable = dtable.drop(dtable.index[0])
                            dtable.columns = new_header
                            dtable.columns = ['RESPONSES' if pd.isna(col) else col for col in dtable.columns]
                            dtable.reset_index(drop=True,inplace=True)
                            
                            df = dtable[dtable['RESPONSES'] == keyR.upper()]
                            
                            if list(df[keyH.upper()]):
                                n = True
                                new_val = list(df[keyH])[0]
                                new_val = 0 if str(new_val) == '*' else new_val
                                new_df.append([slide,obj,size,index,header,categories,ppt_value,
                                            new_val,keyQ,keyR,keyH,tipe,info])
                if n == False:
                    new_df.append([slide,obj,size,index,header,categories,ppt_value,'',key_ques,key_resp,key_head,tipe,info])             
            
            columns = ["Slide","Object","Size","Index","Header","Categories","PPT Value","Revised Value","Key Question","Key Response","Key Header","Type","Info"]

            df = pd.DataFrame(new_df,columns=columns)
            df.to_excel(writer,sheet_name="Data", index=False)

            workbook = writer.book
            worksheet = writer.sheets["Data"]
            worksheet.freeze_panes = 'A2'


