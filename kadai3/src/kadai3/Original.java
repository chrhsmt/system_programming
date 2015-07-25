/**
 * The MIT License (MIT)
 * 
 * Copyright (c) 2015 chihiro hashimoto
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package kadai3;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;

/**
 * Original Object for JCF test.
 * @author chihiro.hashimoto<a14z6ch@aiit.ac.jp>
 *
 */
public class Original implements Serializable {

	/** serialVersionUID. */
	private static final long serialVersionUID = 7156130128386982099L;

	/** id. */
	private int id;

	/** 名前. */
	private String name;

	public Original() {
	}

	public Original(int id, String name) {
		this.id = id;
		this.name = name;
	}

	/**
	 * @return the id
	 */
	public int getId() {
		return id;
	}

	/**
	 * @param id the id to set
	 */
	public void setId(int id) {
		this.id = id;
	}

	/**
	 * @return the name
	 */
	public String getName() {
		return name;
	}

	/**
	 * @param name the name to set
	 */
	public void setName(String name) {
		this.name = name;
	}
	
	@Override
	public boolean equals(Object obj) {
		return EqualsBuilder.reflectionEquals(this, obj);
	}

	@Override
	public int hashCode() {
		return HashCodeBuilder.reflectionHashCode(this);
	}

	/** 
	 * main.
	 * @param args
	 */
	public static void main(String[] args) {
		
		// equals
		Original first = new Original(1, "name");
		Original second = new Original(1, "name");
		Original third = new Original(3, "name");
		assert first.equals(second) : "Not equals";
		assert !first.equals(third) : "Invalid";

		Original target = new Original(1, "name");
		List<Original> list = new ArrayList<Original>();
		list.add(first);
		list.add(second);
		list.add(third);
		
		assert list.contains(target) : "Not implement(equals)";
		
		Map<Original, String> map = new HashMap<Original, String>();
		map.put(first, "");
		map.put(second, "");
		map.put(third, "");
		
		assert map.containsKey(target) : "Not implement(hashCode)";
		
		System.out.println("all ok");
		System.exit(0);
	}
}
