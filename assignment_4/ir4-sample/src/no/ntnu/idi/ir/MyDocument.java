package no.ntnu.idi.ir;


import java.io.File;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.FieldType;

/*
 * The task is to update the given `MyDocument' class (i.e implement the 'Document(File F)' method) to index the following fields per document:
 *
 * - path, the path of the file
 * - from, whatever is stored in the from field of the given message
 * - subject, the subject of the e-mail
 * - contents, the actual e-mail contents
 *
 * All `from', `subject', and `contents' should be searchable, i.e. store their re-spective term vectors. 
 * Look at the given `NewsDocument' class that reads a text file and has better methods for `from', `subject', and `contents'.
 *
 * =============
 *
 * Lucene official documentation: 
 * http://lucene.apache.org/core/4_10_1/index.html
 *
 * Useful resources: 
 *   http://oak.cs.ucla.edu/cs144/projects/lucene/
 *   http://lingpipe-blog.com/2014/03/08/lucene-4-essentials-for-text-search-and-indexing/
 * 
 */


public class MyDocument{

	public static Document Document(File f) throws java.io.FileNotFoundException{

		// make a new, empty document
		Document doc = new Document();

		// use the news document wrapper
		NewsDocument news_doc = new NewsDocument(f);

		//TODO: create structured lucene document
		
		FieldType fieldtype = new FieldType();
		fieldtype.setIndexed(true);
		fieldtype.setTokenized(true);
		fieldtype.setStored(true);
		fieldtype.freeze();
		
		
		doc.add(new Field("ID", news_doc.getId(), fieldtype));
		doc.add(new Field("FROM", news_doc.getFrom(), fieldtype));
		doc.add(new Field("SUBJECT", news_doc.getSubject(), fieldtype));
		doc.add(new Field("CONTENT", news_doc.getContent(), fieldtype));
		
		return doc;
	}

}
