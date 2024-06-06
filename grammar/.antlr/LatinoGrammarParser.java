// Generated from /Users/nataliaquiroga/Desktop/Traductor/grammar/LatinoGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class LatinoGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, AssignOp=14, NumericOp=15, StringOp=16, 
		LogicOp=17, RUnaryOperator=18, LUnaryOperator=19, OperableBuiltInFuncWords=20, 
		ID=21, Tkn_real=22, ESP=23;
	public static final int
		RULE_inicio = 0, RULE_source = 1, RULE_sentencia = 2, RULE_assignableId = 3, 
		RULE_mutableId = 4, RULE_mutableIdModifierConcat = 5, RULE_assignableIdConcat = 6, 
		RULE_sentenciaId = 7, RULE_assignableValue = 8, RULE_assignableExpr = 9, 
		RULE_assignExprConcat = 10, RULE_functionCall = 11, RULE_functionCallArgs = 12, 
		RULE_functionCallArgsConcat = 13, RULE_functionCallSingleArg = 14, RULE_expr = 15, 
		RULE_mutableIdModifier = 16, RULE_objectProperty = 17, RULE_listAcess = 18, 
		RULE_binaryOp = 19, RULE_idExp = 20, RULE_idModifier = 21, RULE_terminal = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"inicio", "source", "sentencia", "assignableId", "mutableId", "mutableIdModifierConcat", 
			"assignableIdConcat", "sentenciaId", "assignableValue", "assignableExpr", 
			"assignExprConcat", "functionCall", "functionCallArgs", "functionCallArgsConcat", 
			"functionCallSingleArg", "expr", "mutableIdModifier", "objectProperty", 
			"listAcess", "binaryOp", "idExp", "idModifier", "terminal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'hola'", "','", "'romper'", "'leer'", "'('", "')'", "'.'", "'['", 
			"']'", "'nulo'", "'falso'", "'cierto'", "'verdadero'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "AssignOp", "NumericOp", "StringOp", "LogicOp", "RUnaryOperator", 
			"LUnaryOperator", "OperableBuiltInFuncWords", "ID", "Tkn_real", "ESP"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "LatinoGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LatinoGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InicioContext extends ParserRuleContext {
		public TerminalContext terminal() {
			return getRuleContext(TerminalContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(LatinoGrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(LatinoGrammarParser.ID, i);
		}
		public InicioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicio; }
	}

	public final InicioContext inicio() throws RecognitionException {
		InicioContext _localctx = new InicioContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_inicio);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(T__0);
			setState(47);
			terminal();
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(48);
				match(T__1);
				setState(49);
				match(ID);
				}
				}
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SourceContext extends ParserRuleContext {
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public SourceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_source; }
	}

	public final SourceContext source() throws RecognitionException {
		SourceContext _localctx = new SourceContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_source);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2 || _la==ID) {
				{
				{
				setState(55);
				sentencia();
				}
				}
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaContext extends ParserRuleContext {
		public AssignableIdContext assignableId() {
			return getRuleContext(AssignableIdContext.class,0);
		}
		public SentenciaIdContext sentenciaId() {
			return getRuleContext(SentenciaIdContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_sentencia);
		try {
			setState(65);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(61);
				assignableId();
				setState(62);
				sentenciaId();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(64);
				match(T__2);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignableIdContext extends ParserRuleContext {
		public MutableIdContext mutableId() {
			return getRuleContext(MutableIdContext.class,0);
		}
		public AssignableIdConcatContext assignableIdConcat() {
			return getRuleContext(AssignableIdConcatContext.class,0);
		}
		public AssignableIdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignableId; }
	}

	public final AssignableIdContext assignableId() throws RecognitionException {
		AssignableIdContext _localctx = new AssignableIdContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assignableId);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			mutableId();
			setState(68);
			assignableIdConcat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MutableIdContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LatinoGrammarParser.ID, 0); }
		public MutableIdModifierConcatContext mutableIdModifierConcat() {
			return getRuleContext(MutableIdModifierConcatContext.class,0);
		}
		public MutableIdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mutableId; }
	}

	public final MutableIdContext mutableId() throws RecognitionException {
		MutableIdContext _localctx = new MutableIdContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_mutableId);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(ID);
			setState(71);
			mutableIdModifierConcat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MutableIdModifierConcatContext extends ParserRuleContext {
		public List<MutableIdModifierContext> mutableIdModifier() {
			return getRuleContexts(MutableIdModifierContext.class);
		}
		public MutableIdModifierContext mutableIdModifier(int i) {
			return getRuleContext(MutableIdModifierContext.class,i);
		}
		public MutableIdModifierConcatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mutableIdModifierConcat; }
	}

	public final MutableIdModifierConcatContext mutableIdModifierConcat() throws RecognitionException {
		MutableIdModifierConcatContext _localctx = new MutableIdModifierConcatContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_mutableIdModifierConcat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6 || _la==T__7) {
				{
				{
				setState(73);
				mutableIdModifier();
				}
				}
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignableIdConcatContext extends ParserRuleContext {
		public List<AssignableIdContext> assignableId() {
			return getRuleContexts(AssignableIdContext.class);
		}
		public AssignableIdContext assignableId(int i) {
			return getRuleContext(AssignableIdContext.class,i);
		}
		public AssignableIdConcatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignableIdConcat; }
	}

	public final AssignableIdConcatContext assignableIdConcat() throws RecognitionException {
		AssignableIdConcatContext _localctx = new AssignableIdConcatContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assignableIdConcat);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(79);
					match(T__1);
					setState(80);
					assignableId();
					}
					} 
				}
				setState(85);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenciaIdContext extends ParserRuleContext {
		public TerminalNode AssignOp() { return getToken(LatinoGrammarParser.AssignOp, 0); }
		public AssignableValueContext assignableValue() {
			return getRuleContext(AssignableValueContext.class,0);
		}
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public TerminalNode RUnaryOperator() { return getToken(LatinoGrammarParser.RUnaryOperator, 0); }
		public SentenciaIdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentenciaId; }
	}

	public final SentenciaIdContext sentenciaId() throws RecognitionException {
		SentenciaIdContext _localctx = new SentenciaIdContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_sentenciaId);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AssignOp:
				enterOuterAlt(_localctx, 1);
				{
				setState(86);
				match(AssignOp);
				setState(87);
				assignableValue();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(88);
				functionCall();
				}
				break;
			case RUnaryOperator:
				enterOuterAlt(_localctx, 3);
				{
				setState(89);
				match(RUnaryOperator);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignableValueContext extends ParserRuleContext {
		public AssignableExprContext assignableExpr() {
			return getRuleContext(AssignableExprContext.class,0);
		}
		public AssignableValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignableValue; }
	}

	public final AssignableValueContext assignableValue() throws RecognitionException {
		AssignableValueContext _localctx = new AssignableValueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_assignableValue);
		try {
			setState(96);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case LUnaryOperator:
			case OperableBuiltInFuncWords:
			case ID:
			case Tkn_real:
				enterOuterAlt(_localctx, 1);
				{
				setState(92);
				assignableExpr();
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 2);
				{
				setState(93);
				match(T__3);
				setState(94);
				match(T__4);
				setState(95);
				match(T__5);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignableExprContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignExprConcatContext assignExprConcat() {
			return getRuleContext(AssignExprConcatContext.class,0);
		}
		public AssignableExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignableExpr; }
	}

	public final AssignableExprContext assignableExpr() throws RecognitionException {
		AssignableExprContext _localctx = new AssignableExprContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_assignableExpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			expr(0);
			setState(99);
			assignExprConcat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignExprConcatContext extends ParserRuleContext {
		public List<AssignableExprContext> assignableExpr() {
			return getRuleContexts(AssignableExprContext.class);
		}
		public AssignableExprContext assignableExpr(int i) {
			return getRuleContext(AssignableExprContext.class,i);
		}
		public AssignExprConcatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignExprConcat; }
	}

	public final AssignExprConcatContext assignExprConcat() throws RecognitionException {
		AssignExprConcatContext _localctx = new AssignExprConcatContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_assignExprConcat);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(101);
					match(T__1);
					setState(102);
					assignableExpr();
					}
					} 
				}
				setState(107);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public FunctionCallArgsContext functionCallArgs() {
			return getRuleContext(FunctionCallArgsContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_functionCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(T__4);
			setState(109);
			functionCallArgs();
			setState(110);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallArgsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<FunctionCallArgsConcatContext> functionCallArgsConcat() {
			return getRuleContexts(FunctionCallArgsConcatContext.class);
		}
		public FunctionCallArgsConcatContext functionCallArgsConcat(int i) {
			return getRuleContext(FunctionCallArgsConcatContext.class,i);
		}
		public FunctionCallArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallArgs; }
	}

	public final FunctionCallArgsContext functionCallArgs() throws RecognitionException {
		FunctionCallArgsContext _localctx = new FunctionCallArgsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_functionCallArgs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7879712L) != 0)) {
				{
				{
				setState(112);
				expr(0);
				setState(113);
				functionCallArgsConcat();
				}
				}
				setState(119);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallArgsConcatContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public FunctionCallArgsConcatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallArgsConcat; }
	}

	public final FunctionCallArgsConcatContext functionCallArgsConcat() throws RecognitionException {
		FunctionCallArgsConcatContext _localctx = new FunctionCallArgsConcatContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_functionCallArgsConcat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(120);
				match(T__1);
				setState(121);
				expr(0);
				}
				}
				setState(126);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallSingleArgContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public FunctionCallSingleArgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallSingleArg; }
	}

	public final FunctionCallSingleArgContext functionCallSingleArg() throws RecognitionException {
		FunctionCallSingleArgContext _localctx = new FunctionCallSingleArgContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_functionCallSingleArg);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			match(T__4);
			setState(128);
			expr(0);
			setState(129);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BinaryOpContext binaryOp() {
			return getRuleContext(BinaryOpContext.class,0);
		}
		public TerminalContext terminal() {
			return getRuleContext(TerminalContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				{
				setState(132);
				match(T__4);
				setState(133);
				expr(0);
				setState(134);
				match(T__5);
				setState(135);
				binaryOp();
				setState(136);
				expr(2);
				}
				break;
			case T__9:
			case T__10:
			case T__11:
			case T__12:
			case LUnaryOperator:
			case OperableBuiltInFuncWords:
			case ID:
			case Tkn_real:
				{
				setState(138);
				terminal();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(147);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(141);
					if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
					setState(142);
					binaryOp();
					setState(143);
					expr(4);
					}
					} 
				}
				setState(149);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MutableIdModifierContext extends ParserRuleContext {
		public ObjectPropertyContext objectProperty() {
			return getRuleContext(ObjectPropertyContext.class,0);
		}
		public ListAcessContext listAcess() {
			return getRuleContext(ListAcessContext.class,0);
		}
		public MutableIdModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mutableIdModifier; }
	}

	public final MutableIdModifierContext mutableIdModifier() throws RecognitionException {
		MutableIdModifierContext _localctx = new MutableIdModifierContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_mutableIdModifier);
		try {
			setState(152);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(150);
				objectProperty();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				listAcess();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ObjectPropertyContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LatinoGrammarParser.ID, 0); }
		public ObjectPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_objectProperty; }
	}

	public final ObjectPropertyContext objectProperty() throws RecognitionException {
		ObjectPropertyContext _localctx = new ObjectPropertyContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_objectProperty);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(T__6);
			setState(155);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListAcessContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ListAcessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listAcess; }
	}

	public final ListAcessContext listAcess() throws RecognitionException {
		ListAcessContext _localctx = new ListAcessContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_listAcess);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(T__7);
			setState(158);
			expr(0);
			setState(159);
			match(T__8);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BinaryOpContext extends ParserRuleContext {
		public TerminalNode NumericOp() { return getToken(LatinoGrammarParser.NumericOp, 0); }
		public TerminalNode StringOp() { return getToken(LatinoGrammarParser.StringOp, 0); }
		public TerminalNode LogicOp() { return getToken(LatinoGrammarParser.LogicOp, 0); }
		public BinaryOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binaryOp; }
	}

	public final BinaryOpContext binaryOp() throws RecognitionException {
		BinaryOpContext _localctx = new BinaryOpContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_binaryOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 229376L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdExpContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(LatinoGrammarParser.ID, 0); }
		public IdModifierContext idModifier() {
			return getRuleContext(IdModifierContext.class,0);
		}
		public IdExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idExp; }
	}

	public final IdExpContext idExp() throws RecognitionException {
		IdExpContext _localctx = new IdExpContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_idExp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(ID);
			setState(164);
			idModifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdModifierContext extends ParserRuleContext {
		public List<MutableIdModifierContext> mutableIdModifier() {
			return getRuleContexts(MutableIdModifierContext.class);
		}
		public MutableIdModifierContext mutableIdModifier(int i) {
			return getRuleContext(MutableIdModifierContext.class,i);
		}
		public List<FunctionCallContext> functionCall() {
			return getRuleContexts(FunctionCallContext.class);
		}
		public FunctionCallContext functionCall(int i) {
			return getRuleContext(FunctionCallContext.class,i);
		}
		public IdModifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idModifier; }
	}

	public final IdModifierContext idModifier() throws RecognitionException {
		IdModifierContext _localctx = new IdModifierContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_idModifier);
		try {
			int _alt;
			setState(178);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(169);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(166);
						mutableIdModifier();
						}
						} 
					}
					setState(171);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(175);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(172);
						functionCall();
						}
						} 
					}
					setState(177);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminalContext extends ParserRuleContext {
		public TerminalNode Tkn_real() { return getToken(LatinoGrammarParser.Tkn_real, 0); }
		public IdExpContext idExp() {
			return getRuleContext(IdExpContext.class,0);
		}
		public TerminalNode LUnaryOperator() { return getToken(LatinoGrammarParser.LUnaryOperator, 0); }
		public TerminalContext terminal() {
			return getRuleContext(TerminalContext.class,0);
		}
		public TerminalNode OperableBuiltInFuncWords() { return getToken(LatinoGrammarParser.OperableBuiltInFuncWords, 0); }
		public FunctionCallSingleArgContext functionCallSingleArg() {
			return getRuleContext(FunctionCallSingleArgContext.class,0);
		}
		public TerminalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminal; }
	}

	public final TerminalContext terminal() throws RecognitionException {
		TerminalContext _localctx = new TerminalContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_terminal);
		try {
			setState(190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(180);
				match(T__9);
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				match(T__10);
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 3);
				{
				setState(182);
				match(T__11);
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 4);
				{
				setState(183);
				match(T__12);
				}
				break;
			case Tkn_real:
				enterOuterAlt(_localctx, 5);
				{
				setState(184);
				match(Tkn_real);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 6);
				{
				setState(185);
				idExp();
				}
				break;
			case LUnaryOperator:
				enterOuterAlt(_localctx, 7);
				{
				setState(186);
				match(LUnaryOperator);
				setState(187);
				terminal();
				}
				break;
			case OperableBuiltInFuncWords:
				enterOuterAlt(_localctx, 8);
				{
				setState(188);
				match(OperableBuiltInFuncWords);
				setState(189);
				functionCallSingleArg();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 15:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0017\u00c1\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0005\u00003\b\u0000\n\u0000\f\u00006\t\u0000\u0001\u0001\u0005"+
		"\u00019\b\u0001\n\u0001\f\u0001<\t\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002B\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0005\u0005K\b"+
		"\u0005\n\u0005\f\u0005N\t\u0005\u0001\u0006\u0001\u0006\u0005\u0006R\b"+
		"\u0006\n\u0006\f\u0006U\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0003\u0007[\b\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0003\ba\b"+
		"\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0005\nh\b\n\n\n\f\nk\t\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0005"+
		"\ft\b\f\n\f\f\fw\t\f\u0001\r\u0001\r\u0005\r{\b\r\n\r\f\r~\t\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u008c\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f"+
		"\u0092\b\u000f\n\u000f\f\u000f\u0095\t\u000f\u0001\u0010\u0001\u0010\u0003"+
		"\u0010\u0099\b\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0015\u0005\u0015\u00a8\b\u0015\n\u0015\f\u0015"+
		"\u00ab\t\u0015\u0001\u0015\u0005\u0015\u00ae\b\u0015\n\u0015\f\u0015\u00b1"+
		"\t\u0015\u0003\u0015\u00b3\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0003\u0016\u00bf\b\u0016\u0001\u0016\u0000\u0001\u001e\u0017"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u001c\u001e \"$&(*,\u0000\u0001\u0001\u0000\u000f\u0011\u00c1\u0000."+
		"\u0001\u0000\u0000\u0000\u0002:\u0001\u0000\u0000\u0000\u0004A\u0001\u0000"+
		"\u0000\u0000\u0006C\u0001\u0000\u0000\u0000\bF\u0001\u0000\u0000\u0000"+
		"\nL\u0001\u0000\u0000\u0000\fS\u0001\u0000\u0000\u0000\u000eZ\u0001\u0000"+
		"\u0000\u0000\u0010`\u0001\u0000\u0000\u0000\u0012b\u0001\u0000\u0000\u0000"+
		"\u0014i\u0001\u0000\u0000\u0000\u0016l\u0001\u0000\u0000\u0000\u0018u"+
		"\u0001\u0000\u0000\u0000\u001a|\u0001\u0000\u0000\u0000\u001c\u007f\u0001"+
		"\u0000\u0000\u0000\u001e\u008b\u0001\u0000\u0000\u0000 \u0098\u0001\u0000"+
		"\u0000\u0000\"\u009a\u0001\u0000\u0000\u0000$\u009d\u0001\u0000\u0000"+
		"\u0000&\u00a1\u0001\u0000\u0000\u0000(\u00a3\u0001\u0000\u0000\u0000*"+
		"\u00b2\u0001\u0000\u0000\u0000,\u00be\u0001\u0000\u0000\u0000./\u0005"+
		"\u0001\u0000\u0000/4\u0003,\u0016\u000001\u0005\u0002\u0000\u000013\u0005"+
		"\u0015\u0000\u000020\u0001\u0000\u0000\u000036\u0001\u0000\u0000\u0000"+
		"42\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u00005\u0001\u0001\u0000"+
		"\u0000\u000064\u0001\u0000\u0000\u000079\u0003\u0004\u0002\u000087\u0001"+
		"\u0000\u0000\u00009<\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000"+
		":;\u0001\u0000\u0000\u0000;\u0003\u0001\u0000\u0000\u0000<:\u0001\u0000"+
		"\u0000\u0000=>\u0003\u0006\u0003\u0000>?\u0003\u000e\u0007\u0000?B\u0001"+
		"\u0000\u0000\u0000@B\u0005\u0003\u0000\u0000A=\u0001\u0000\u0000\u0000"+
		"A@\u0001\u0000\u0000\u0000B\u0005\u0001\u0000\u0000\u0000CD\u0003\b\u0004"+
		"\u0000DE\u0003\f\u0006\u0000E\u0007\u0001\u0000\u0000\u0000FG\u0005\u0015"+
		"\u0000\u0000GH\u0003\n\u0005\u0000H\t\u0001\u0000\u0000\u0000IK\u0003"+
		" \u0010\u0000JI\u0001\u0000\u0000\u0000KN\u0001\u0000\u0000\u0000LJ\u0001"+
		"\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000M\u000b\u0001\u0000\u0000"+
		"\u0000NL\u0001\u0000\u0000\u0000OP\u0005\u0002\u0000\u0000PR\u0003\u0006"+
		"\u0003\u0000QO\u0001\u0000\u0000\u0000RU\u0001\u0000\u0000\u0000SQ\u0001"+
		"\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000T\r\u0001\u0000\u0000\u0000"+
		"US\u0001\u0000\u0000\u0000VW\u0005\u000e\u0000\u0000W[\u0003\u0010\b\u0000"+
		"X[\u0003\u0016\u000b\u0000Y[\u0005\u0012\u0000\u0000ZV\u0001\u0000\u0000"+
		"\u0000ZX\u0001\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[\u000f\u0001"+
		"\u0000\u0000\u0000\\a\u0003\u0012\t\u0000]^\u0005\u0004\u0000\u0000^_"+
		"\u0005\u0005\u0000\u0000_a\u0005\u0006\u0000\u0000`\\\u0001\u0000\u0000"+
		"\u0000`]\u0001\u0000\u0000\u0000a\u0011\u0001\u0000\u0000\u0000bc\u0003"+
		"\u001e\u000f\u0000cd\u0003\u0014\n\u0000d\u0013\u0001\u0000\u0000\u0000"+
		"ef\u0005\u0002\u0000\u0000fh\u0003\u0012\t\u0000ge\u0001\u0000\u0000\u0000"+
		"hk\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000"+
		"\u0000j\u0015\u0001\u0000\u0000\u0000ki\u0001\u0000\u0000\u0000lm\u0005"+
		"\u0005\u0000\u0000mn\u0003\u0018\f\u0000no\u0005\u0006\u0000\u0000o\u0017"+
		"\u0001\u0000\u0000\u0000pq\u0003\u001e\u000f\u0000qr\u0003\u001a\r\u0000"+
		"rt\u0001\u0000\u0000\u0000sp\u0001\u0000\u0000\u0000tw\u0001\u0000\u0000"+
		"\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000\u0000v\u0019\u0001"+
		"\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000xy\u0005\u0002\u0000\u0000"+
		"y{\u0003\u001e\u000f\u0000zx\u0001\u0000\u0000\u0000{~\u0001\u0000\u0000"+
		"\u0000|z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}\u001b\u0001"+
		"\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000\u007f\u0080\u0005\u0005\u0000"+
		"\u0000\u0080\u0081\u0003\u001e\u000f\u0000\u0081\u0082\u0005\u0006\u0000"+
		"\u0000\u0082\u001d\u0001\u0000\u0000\u0000\u0083\u0084\u0006\u000f\uffff"+
		"\uffff\u0000\u0084\u0085\u0005\u0005\u0000\u0000\u0085\u0086\u0003\u001e"+
		"\u000f\u0000\u0086\u0087\u0005\u0006\u0000\u0000\u0087\u0088\u0003&\u0013"+
		"\u0000\u0088\u0089\u0003\u001e\u000f\u0002\u0089\u008c\u0001\u0000\u0000"+
		"\u0000\u008a\u008c\u0003,\u0016\u0000\u008b\u0083\u0001\u0000\u0000\u0000"+
		"\u008b\u008a\u0001\u0000\u0000\u0000\u008c\u0093\u0001\u0000\u0000\u0000"+
		"\u008d\u008e\n\u0003\u0000\u0000\u008e\u008f\u0003&\u0013\u0000\u008f"+
		"\u0090\u0003\u001e\u000f\u0004\u0090\u0092\u0001\u0000\u0000\u0000\u0091"+
		"\u008d\u0001\u0000\u0000\u0000\u0092\u0095\u0001\u0000\u0000\u0000\u0093"+
		"\u0091\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094"+
		"\u001f\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000\u0000\u0096"+
		"\u0099\u0003\"\u0011\u0000\u0097\u0099\u0003$\u0012\u0000\u0098\u0096"+
		"\u0001\u0000\u0000\u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0099!\u0001"+
		"\u0000\u0000\u0000\u009a\u009b\u0005\u0007\u0000\u0000\u009b\u009c\u0005"+
		"\u0015\u0000\u0000\u009c#\u0001\u0000\u0000\u0000\u009d\u009e\u0005\b"+
		"\u0000\u0000\u009e\u009f\u0003\u001e\u000f\u0000\u009f\u00a0\u0005\t\u0000"+
		"\u0000\u00a0%\u0001\u0000\u0000\u0000\u00a1\u00a2\u0007\u0000\u0000\u0000"+
		"\u00a2\'\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005\u0015\u0000\u0000\u00a4"+
		"\u00a5\u0003*\u0015\u0000\u00a5)\u0001\u0000\u0000\u0000\u00a6\u00a8\u0003"+
		" \u0010\u0000\u00a7\u00a6\u0001\u0000\u0000\u0000\u00a8\u00ab\u0001\u0000"+
		"\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000"+
		"\u0000\u0000\u00aa\u00b3\u0001\u0000\u0000\u0000\u00ab\u00a9\u0001\u0000"+
		"\u0000\u0000\u00ac\u00ae\u0003\u0016\u000b\u0000\u00ad\u00ac\u0001\u0000"+
		"\u0000\u0000\u00ae\u00b1\u0001\u0000\u0000\u0000\u00af\u00ad\u0001\u0000"+
		"\u0000\u0000\u00af\u00b0\u0001\u0000\u0000\u0000\u00b0\u00b3\u0001\u0000"+
		"\u0000\u0000\u00b1\u00af\u0001\u0000\u0000\u0000\u00b2\u00a9\u0001\u0000"+
		"\u0000\u0000\u00b2\u00af\u0001\u0000\u0000\u0000\u00b3+\u0001\u0000\u0000"+
		"\u0000\u00b4\u00bf\u0005\n\u0000\u0000\u00b5\u00bf\u0005\u000b\u0000\u0000"+
		"\u00b6\u00bf\u0005\f\u0000\u0000\u00b7\u00bf\u0005\r\u0000\u0000\u00b8"+
		"\u00bf\u0005\u0016\u0000\u0000\u00b9\u00bf\u0003(\u0014\u0000\u00ba\u00bb"+
		"\u0005\u0013\u0000\u0000\u00bb\u00bf\u0003,\u0016\u0000\u00bc\u00bd\u0005"+
		"\u0014\u0000\u0000\u00bd\u00bf\u0003\u001c\u000e\u0000\u00be\u00b4\u0001"+
		"\u0000\u0000\u0000\u00be\u00b5\u0001\u0000\u0000\u0000\u00be\u00b6\u0001"+
		"\u0000\u0000\u0000\u00be\u00b7\u0001\u0000\u0000\u0000\u00be\u00b8\u0001"+
		"\u0000\u0000\u0000\u00be\u00b9\u0001\u0000\u0000\u0000\u00be\u00ba\u0001"+
		"\u0000\u0000\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00bf-\u0001\u0000"+
		"\u0000\u0000\u00114:ALSZ`iu|\u008b\u0093\u0098\u00a9\u00af\u00b2\u00be";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}