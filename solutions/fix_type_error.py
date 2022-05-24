cleaned_df['lat'] = cleaned_df['lat'].astype('float').map(reduce_precision)
cleaned_df['long'] = cleaned_df['long'].astype('float').map(reduce_precision)
