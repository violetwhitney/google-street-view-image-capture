
class SortThumb implements Comparator {
  
  String metricToSortOn;
  
  SortThumb (String metricToSortOn_) {
    metricToSortOn = metricToSortOn_;
  }
  
  public int compare (Object a1, Object a2) {
    if (metricToSortOn == "lotArea") {
      Integer int1 = ((RowThumbnail) a1).lotArea; 
      Integer int2 = ((RowThumbnail) a2).lotArea;
      return int2.compareTo(int1);
    } else if (metricToSortOn == "chron"){ 
      Integer int1 = int(((RowThumbnail) a1).row); 
      Integer int2 = int(((RowThumbnail) a2).row);
      //Integer int1 = int(((RowThumbnail) a1).yearPublished); 
      //Integer int2 = int(((RowThumbnail) a2).yearPublished);
      return int1.compareTo(int2);
    } 
    return 0;
  }
}