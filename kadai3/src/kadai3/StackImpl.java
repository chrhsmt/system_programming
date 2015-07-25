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

import java.util.AbstractCollection;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

/**
 * @link{Stack} クラスの実装.
 * @author chihiro.hashitmo<a14z6ch@aiit.ac.jp>
 *
 */
public class StackImpl<E> extends AbstractCollection<E> implements Stack<E> {

	private static int INITIAL_SIZE = 5;
	
	/** 内部配列. */
	private Object[] stack = new Object[INITIAL_SIZE];
	private int counter = 0;

	public StackImpl() {
	}

	@Override
	public int size() {
		return this.counter;
	}

	@Override
	public Iterator<E> iterator() {
		final Object[] _stack = this.stack;
		final int _counter = this.counter;

		return new Iterator<E>() {

			private int counter = 0;

			@Override
			public boolean hasNext() {
				return counter < _counter;
			}

			@SuppressWarnings("unchecked")
			@Override
			public E next() {
				return (E) _stack[counter++];
			}
		};
	}

	@Override
    public boolean add(E e) {
		if (this.stack.length <= this.counter) {
			this.stack = Arrays.copyOf(this.stack, this.stack.length + INITIAL_SIZE);
		}
		this.stack[this.counter++] = e;
		return true;
	}

	@SuppressWarnings("unchecked")
	@Override
	public E pop() {
		if (this.size() == 0) {
			return null;
		}
		Object last = this.stack[this.counter - 1];
		this.stack[this.counter - 1] = null;
		return (E) last;
	}

	/**
	 * テスト用Main.
	 * @param args
	 */
	public static void main(String[] args) {
		Stack<String> stack = new StackImpl<String>();
		
		stack.add("1st");
		stack.add("2nd");
		stack.add("3rd");
		stack.add("4th");

		List<String> list = new ArrayList<String>();
		list.add("1st");
		list.add("2nd");

		// stackのsizeが正常なこと
		assert stack.size() == 4 : "Invalid size";
		// containsが正常なこと
		assert stack.contains("1st") : "Invalid contains";
		// containsAllが正常なこと
		assert stack.containsAll(list) : "Invalid containsAll";
		// 最期に加えた要素が取得出来ていること
		assert "4th".equals(stack.pop()) : "Invalid pop";
		
		System.out.println("all ok");
		System.exit(0);
	}
}
